from flask_restx import Namespace, Resource, fields, reqparse, abort
from core.database import db, Pokemons, PokemonLocations, Locations

api = Namespace('Pokemons', description='Recurso para pokemons')

basePokemonLocation = api.model(name='BasePokemonLocation', model={
    'codPokemonLocation': fields.Integer,
    'locationCod': fields.Integer,
    'locationName': fields.String(attribute='location.name')
})

basePokemonGame = api.model(name='BasePokemonGame', model={
    'codPokemonGame': fields.Integer,
    'gameCod': fields.Integer,
    'gameName': fields.String(attribute='game.name')
})

basePokemonHability = api.model(name='BasePokemonGame', model={
    'codPokemonHability': fields.Integer,
    'habilityCod': fields.Integer,
    'habilityName': fields.String(attribute='hability.name'),
    'habilityDescription': fields.String(attribute='hability.description')
})

basePokemonMove = api.model(name='BasePokemonMove', model={
    'codPokemonMove': fields.Integer,
    'moveCod': fields.Integer,
    'moveName': fields.String(attribute='move.name'),
    'descriptionName': fields.String(attribute='move.description')
})

basePokemon = api.model(name='BasePokemon', model={
    'codPokemon': fields.Integer,
    'name': fields.String,
    'height': fields.Integer,
    'weight': fields.Integer,
    'hp': fields.Integer,
    'attack': fields.Integer,
    'defense': fields.Integer,
    'specialAttack': fields.Integer,
    'specialDefense': fields.Integer,
    'speed': fields.Integer,
    'pokemonLocations': fields.List(fields.Nested(basePokemonLocation)),
    'pokemonGames': fields.List(fields.Nested(basePokemonGame)),
    'pokemonHabilities': fields.List(fields.Nested(basePokemonHability)),
    'pokemonMoves': fields.List(fields.Nested(basePokemonMove))
})

postPokemon = api.model(name='PostPokemon', model={
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

@api.route('')
class PokemonsResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)

    @api.expect(parser)
    @api.marshal_with(basePokemon, as_list=True)
    def get(self):
        args = self.parser.parse_args()

        query = db.session.query(Pokemons)

        if 'name' in args and args['name'] != None:
            query = query.filter(Pokemons.name.like('%'+args['name']+'%'))

        return query.all()

    @api.expect(postPokemon, validate=True)
    @api.marshal_with(basePokemon)
    def post(self):
        body = api.payload

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

        db.session.add(newPokemon)
        db.session.commit()

        return newPokemon
    
@api.route('/<int:codPokemon>')
class PokemonsResource(Resource):

    @api.marshal_with(basePokemon)
    def get(self, codPokemon: int):
        pokemon: Pokemons = db.session.query(Pokemons).get(codPokemon)
        if pokemon == None:
            abort(404, 'No se encuentra el pokemon')

        return pokemon
    
    @api.expect(postPokemon, validate=True)
    @api.marshal_with(basePokemon)
    def put(self, codPokemon: int):
        body = api.payload

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
            db.session.commit()
        except:
            abort(500)
        
        return pokemon