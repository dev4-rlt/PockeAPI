from flask_restx import Namespace, Resource, fields, reqparse, abort
from core.database import db, Pokemons
from apis.models import pokemonModel, pokemonLocationModel, pokemonGameModel, pokemonAbilityModel, pokemonMoveModel, pgModel, postLocation, postGame, postAbility, postMove
from core.database.ability import Habilities
from core.database.game import Games
from core.database.location import Locations
from core.database.move import Moves
from core.database.pokemon_games import PokemonGames
from core.database.pokemon_habilities import PokemonHabilities
from core.database.pokemon_locations import PokemonLocations
from core.database.pokemon_moves import PokemonMoves

namespace = Namespace('Pokemons', description='Recurso para pokemons')

pokemonDetails = namespace.inherit('PokemonDetails', pokemonModel, {
    'pokemonLocations': fields.List(fields.Nested(pokemonLocationModel)),
    'pokemonGames': fields.List(fields.Nested(pokemonGameModel)),
    'pokemonHabilities': fields.List(fields.Nested(pokemonAbilityModel)),
    'pokemonMoves': fields.List(fields.Nested(pokemonMoveModel))
})

pgPokemon = namespace.inherit('PgPokemon', pgModel, {
    'items': fields.List(fields.Nested(pokemonModel))
})

postPokemon = namespace.model(name='PostPokemon', model={
    'name': fields.String,
    'height': fields.Integer,
    'weight': fields.Integer,
    'hp': fields.Integer,
    'attack': fields.Integer,
    'defense': fields.Integer,
    'specialAttack': fields.Integer,
    'specialDefense': fields.Integer,
    'speed': fields.Integer, 
})

postCompletePokemon = namespace.model(name='PostCompletePokemon', model={
    'name': fields.String,
    'height': fields.Integer,
    'weight': fields.Integer,
    'hp': fields.Integer,
    'attack': fields.Integer,
    'defense': fields.Integer,
    'specialAttack': fields.Integer,
    'specialDefense': fields.Integer,
    'speed': fields.Integer,
    'spriteFrontDefault': fields.String,
    'spriteFrontShiny': fields.String,
    'pokemonLocations': fields.List(fields.Nested(postLocation)),
    'pokemonGames': fields.List(fields.Nested(postGame)),
    'pokemonHabilities': fields.List(fields.Nested(postAbility)),
    'pokemonMoves': fields.List(fields.Nested(postMove))
})

@namespace.route('')
class PokemonsResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)
    parser.add_argument('page', type=int)
    parser.add_argument('per_page', type=int)

    @namespace.expect(parser, validate=True)
    @namespace.marshal_with(pgPokemon)
    def get(self):
        args = self.parser.parse_args()
        query = db.session.query(Pokemons)

        if 'name' in args and args['name'] != None:
            query = query.filter(Pokemons.name.ilike('%'+args['name']+'%'))
            #query = query.filter(Pokemons.name.like('%'+args['name']+'%')) #Case sensitive
        
        #query = query.order_by(Pokemons.codPokemon.desc())
        query = query.order_by(Pokemons.codPokemon)
        
        if 'page' in args and args['page'] != None:
            if 'per_page' in args and args['per_page'] != None:
                return query.paginate(page=int(args['page']), per_page=int(args['per_page']))
        
        return query.paginate(page=1, per_page=25)


        # if 'offset' in args and args['offset'] != None:
        #     query = query.offset(args['offset'])

        # if 'limit' in args and args['limit'] != None:
        #     query = query.limit(args['limit'])
        # else:
        #     query = query.limit(12)


    @namespace.expect(postPokemon, validate=True)
    @namespace.marshal_with(pokemonModel)
    def post(self):
        body = namespace.payload

        newPokemon = Pokemons()
        newPokemon.name = body['name']
        newPokemon.height = body['height']
        newPokemon.weight = body['weight']
        newPokemon.hp = body['hp']
        newPokemon.attack = body['attack']
        newPokemon.defense = body['defense']
        newPokemon.specialAttack = body['specialAttack']
        newPokemon.specialDefense = body['specialDefense']
        newPokemon.speed = body['speed']
        newPokemon.spriteFrontDefault = body['spriteFrontDefault']
        newPokemon.spriteFrontShiny = body['spriteFrontShiny']

        db.session.add(newPokemon)
        db.session.commit()

        return newPokemon
    
@namespace.route('/details')
class PokemonsDetailsResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('codPokemon', type=int)

    @namespace.expect(parser)
    @namespace.marshal_with(pokemonDetails)
    def get(self):
        args = self.parser.parse_args()

        query = db.session.query(Pokemons)

        if 'codPokemon' in args and args['codPokemon'] != None:
            query = query.filter(Pokemons.codPokemon == args['codPokemon'])
        
        return query.first()
    
     
    @namespace.expect(postCompletePokemon, validate=True)
    @namespace.marshal_with(pokemonDetails)
    def post(self):

        body = namespace.payload

        newPokemon = Pokemons()
        newPokemon.name = body['name'].capitalize()
        newPokemon.height = body['height']
        newPokemon.weight = body['weight']
        newPokemon.hp = body['hp']
        newPokemon.attack = body['attack']
        newPokemon.defense = body['defense']
        newPokemon.specialAttack = body['specialAttack']
        newPokemon.specialDefense = body['specialDefense']
        newPokemon.speed = body['speed']
        newPokemon.spriteFrontDefault = body['spriteFrontDefault']
        newPokemon.spriteFrontShiny = body['spriteFrontShiny']
        
        for ability in body['pokemonHabilities']:
            savedAbility: Habilities = db.session.query(Habilities).filter(Habilities.name == ability['name'].capitalize()).first()
                
            pokemonAbility = PokemonHabilities()
            if savedAbility is None:
                newAbility = Habilities()
                newAbility.name = ability['name'].capitalize()

                newAbility.description = ability['description']
                db.session.add(newAbility)
                pokemonAbility.ability = newAbility
            else:
                pokemonAbility.abilityCod = savedAbility.codHability
            
            newPokemon.pokemonHabilities.append(pokemonAbility)
        
        for location in body['pokemonLocations']:
            savedLocation: Locations = db.session.query(Locations).filter(Locations.name == location['name'].capitalize()).first()

            pokemonLocation = PokemonLocations()
            if savedLocation is None:
                newLocation = Locations()
                newLocation.name = location['name']

                db.session.add(newLocation)
                pokemonLocation.location = newLocation
            else:
                pokemonLocation.locationCod = savedLocation.codLocation
            
            newPokemon.pokemonLocations.append(pokemonLocation)
        
        for move in  body['pokemonMoves']:
            savedMove: Moves = db.session.query(Moves).filter(Moves.name == move['name'].capitalize()).first()
                
            pokemonMove = PokemonMoves()
            if savedMove is None:
                newMove = Moves()
                newMove.name = move['name'].capitalize()

                newMove.description = move['description']
                db.session.add(newMove)
                pokemonMove.move = newMove
            else:
                pokemonMove.moveCod = savedMove.codMove
            
            newPokemon.pokemonMoves.append(pokemonMove)
        
        for game in  body['pokemonGames']:
            savedGame: Games = db.session.query(Games).filter(Games.name == game['name'].capitalize()).first()

            pokemonGame = PokemonGames()
            if savedGame is None:
                newGame = Games()
                newGame.name = game['name'].capitalize()

                db.session.add(newGame)
                pokemonGame.game = newGame
            else:
                pokemonGame.gameCod = savedGame.codGame
            
            newPokemon.pokemonGames.append(pokemonGame)

        db.session.add(newPokemon)
        db.session.commit()

        return newPokemon
    
@namespace.route('/<int:codPokemon>')
class PokemonsResource(Resource):

    @namespace.marshal_with(pokemonDetails)
    def get(self, codPokemon: int):
        pokemon: Pokemons = db.session.query(Pokemons).get(codPokemon)
        if pokemon == None:
            abort(404, 'No se encuentra el pokemon buscado')

        return pokemon
    
    @namespace.expect(postPokemon, validate=True)
    @namespace.marshal_with(pokemonDetails)
    def put(self, codPokemon: int):
        body = namespace.payload

        pokemon: Pokemons = db.session.query(Pokemons).get(codPokemon)
        if pokemon == None:
            abort(404, 'No se encuentra el pokemon')

        try:
            pokemon.name = body['name']
            pokemon.height = body['height']
            pokemon.weight = body['weight']
            pokemon.hp = body['hp']
            pokemon.attack = body['attack']
            pokemon.defense = body['defense']
            pokemon.specialAttack = body['specialAttack']
            pokemon.specialDefense = body['specialDefense']
            pokemon.speed = body['speed']
            pokemon.spriteFrontDefault = body['spriteFrontDefault']
            pokemon.spriteFrontShiny = body['spriteFrontShiny']
            db.session.commit()
        except:
            abort(500)
        
        return pokemon