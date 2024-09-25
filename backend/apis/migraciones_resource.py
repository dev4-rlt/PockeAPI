from flask_restx import Namespace, Resource, reqparse
from core.database import Pokemons, Habilities, Games, Locations, Moves, db, PokemonHabilities, PokemonGames, PokemonLocations, PokemonMoves
import requests

namespace = Namespace('Migraciones', description='Recurso para migraciones a la base de datos')
POKEMON_LINK = 'https://pokeapi.co/api/v2/pokemon'
ABILITY_LINK = 'https://pokeapi.co/api/v2/ability'
GAME_LINK = 'https://pokeapi.co/api/v2/version'
LOCATION_LINK = 'https://pokeapi.co/api/v2/location-area'
MOVE_LINK = 'https://pokeapi.co/api/v2/move'

def getDescription(descriptions: list) -> str:
    for description in descriptions:
        if description['language']['name'] == 'en':
            return description['flavor_text']
    return None

@namespace.route('/pokemons')
class PokemonMigration(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('offset', type=int)
    parser.add_argument('limit', type=int)

    @namespace.expect(parser, validate=True)
    def post(self):
        args = self.parser.parse_args()
        res = requests.get(POKEMON_LINK, params={'offset':args['offset'], 'limit':args['limit']}).json()

        for pokemon in res['results']:
            savedPokemon: Pokemons = db.session.query(Pokemons).filter(Pokemons.name == pokemon['name'].capitalize()).first()
            if savedPokemon is not None: continue

            pokemonInfo = requests.get(pokemon['url']).json()

            newPokemon = Pokemons()
            newPokemon.name = pokemon['name'].capitalize()
            newPokemon.height = pokemonInfo['height']
            newPokemon.weight = pokemonInfo['weight']
            self.setSprites(pokemonInfo['sprites'], newPokemon)
            
            for stat in pokemonInfo['stats']:
                self.setStatValue(stat, newPokemon)
            
            for ability in pokemonInfo['abilities']:
                savedAbility: Habilities = db.session.query(Habilities).filter(Habilities.name == ability['ability']['name'].capitalize()).first()
                
                pokemonAbility = PokemonHabilities()
                if savedAbility is None:
                    newAbility = Habilities()
                    newAbility.name = ability['ability']['name'].capitalize()

                    abilityDetails = requests.get(ability['ability']['url']).json()
                    newAbility.description = getDescription(abilityDetails['flavor_text_entries'])
                    db.session.add(newAbility)
                    pokemonAbility.ability = newAbility
                else:
                    pokemonAbility.abilityCod = savedAbility.codHability
                
                newPokemon.pokemonHabilities.append(pokemonAbility)

            for game in pokemonInfo['game_indices']:
                savedGame: Games = db.session.query(Games).filter(Games.name == game['version']['name'].capitalize()).first()

                pokemonGame = PokemonGames()
                if savedGame is None:
                    newGame = Games()
                    newGame.name = game['version']['name'].capitalize()

                    db.session.add(newGame)
                    pokemonGame.game = newGame
                else:
                    pokemonGame.gameCod = savedGame.codGame
                
                newPokemon.pokemonGames.append(pokemonGame)
            
            locations = requests.get(pokemonInfo['location_area_encounters']).json()
            for location in locations:
                words: list[str] = location['location_area']['name'].split('-')
                
                locationName = ''
                for word in words:
                    locationName += word.capitalize() + ' '
                locationName.strip()

                savedLocation: Locations = db.session.query(Locations).filter(Locations.name == locationName).first()

                pokemonLocation = PokemonLocations()
                if savedLocation is None:
                    newLocation = Locations()
                    newLocation.name = locationName

                    db.session.add(newLocation)
                    pokemonLocation.location = newLocation
                else:
                    pokemonLocation.locationCod = savedLocation.codLocation
                
                newPokemon.pokemonLocations.append(pokemonLocation)

            for move in pokemonInfo['moves']:
                savedMove: Moves = db.session.query(Moves).filter(Moves.name == move['move']['name'].capitalize()).first()
                
                pokemonMove = PokemonMoves()
                if savedMove is None:
                    newMove = Moves()
                    newMove.name = move['move']['name'].capitalize()

                    moveDetails = requests.get(move['move']['url']).json()
                    newMove.description = getDescription(moveDetails['flavor_text_entries'])
                    db.session.add(newMove)
                    pokemonMove.move = newMove
                else:
                    pokemonMove.moveCod = savedMove.codMove
                
                newPokemon.pokemonMoves.append(pokemonMove)
            
            db.session.add(newPokemon)
        db.session.commit()

        return 'OK'

    def setStatValue(self, stat, pokemon: Pokemons):
        name = stat['stat']['name']
        value = stat['base_stat']

        if name == 'hp':
            pokemon.hp = value
        elif name == 'attack':
            pokemon.attack = value
        elif name == 'defense':
            pokemon.defense = value
        elif name == 'special-attack':
            pokemon.specialAttack = value
        elif name == 'special-defense':
            pokemon.specialDefense = value
        elif name == 'speed':
            pokemon.speed = value

    def setSprites(sprites, pokemon: Pokemons):
        pokemon.spriteFrontDefault = sprites['front_default']
        pokemon.spriteFrontShiny = sprites['front_shiny']

@namespace.route('/abilities')
class AbilityMigration(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('offset', type=int)
    parser.add_argument('limit', type=int)

    @namespace.expect(parser, validate=True)
    def post(self):
        args = self.parser.parse_args()
        res = requests.get(ABILITY_LINK, params={'offset':args['offset'], 'limit':args['limit']}).json()

        abilities: list[Habilities] = []
        for ability in res['results']:
            savedAbility: Habilities = db.session.query(Habilities).filter(Habilities.name == ability['name'].capitalize()).first()  
            if savedAbility is not None:
                continue
                
            abilityInfo = requests.get(ability['url']).json()

            newAbility = Habilities()
            newAbility.name = ability['name'].capitalize()
            newAbility.description = getDescription(abilityInfo['flavor_text_entries'])

            abilities.append(newAbility)
        
        db.session.add_all(abilities)
        db.session.commit()

        return 'OK'

@namespace.route('/games')
class GameMigration(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('offset', type=int)
    parser.add_argument('limit', type=int)

    @namespace.expect(parser, validate=True)
    def post(self):
        args = self.parser.parse_args()
        res = requests.get(GAME_LINK, params={'offset':args['offset'], 'limit':args['limit']}).json()

        games: list[Games] = []
        for game in res['results']:
            savedGame: Games = db.session.query(Games).filter(Games.name == game['name'].capitalize()).first()  
            if savedGame is not None:
                continue

            newGame = Games()
            newGame.name = game['name'].capitalize()

            games.append(newGame)
        
        db.session.add_all(games)
        db.session.commit()

        return 'OK'
    
@namespace.route('/locations')
class LocationMigration(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('offset', type=int)
    parser.add_argument('limit', type=int)

    @namespace.expect(parser, validate=True)
    def post(self):
        args = self.parser.parse_args()
        res = requests.get(LOCATION_LINK, params={'offset':args['offset'], 'limit':args['limit']}).json()

        locations: list[Locations] = []
        for location in res['results']:

            words: list[str] = location['name'].split('-')
            locationName = ''
            for word in words:
                locationName += word.capitalize() + ' '
            locationName.strip()
            
            savedLocation: Locations = db.session.query(Locations).filter(Locations.name == locationName).first()
            if savedLocation is not None:
                continue

            newLocation = Locations()
            newLocation.name = locationName
            locations.append(newLocation)
        
        db.session.add_all(locations)
        db.session.commit()

        return 'OK'
    
@namespace.route('/moves')
class MoveMigration(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('offset', type=int)
    parser.add_argument('limit', type=int)

    @namespace.expect(parser, validate=True)
    def post(self):
        args = self.parser.parse_args()
        res = requests.get(MOVE_LINK, params={'offset':args['offset'], 'limit':args['limit']}).json()

        moves: list[Moves] = []
        for move in res['results']:
            savedMove: Moves = db.session.query(Moves).filter(Moves.name == move['name'].capitalize()).first()  
            if savedMove is not None:
                continue

            moveInfo = requests.get(move['url']).json()

            newMove = Habilities()
            newMove.name = move['name'].capitalize()
            newMove.description = getDescription(moveInfo['flavor_text_entries'])

            moves.append(newMove)
        
        db.session.add_all(moves)
        db.session.commit()

        return 'OK'