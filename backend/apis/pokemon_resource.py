from flask_restx import Namespace, Resource, fields, reqparse, abort
from core.database import db, Pokemons

api = Namespace('Pokemons', description='Recurso para pokemons')

basePokemon = api.model(name='BasePokemon', model={
    'cod_pokemon': fields.Integer,
    'name': fields.String,
    'height': fields.Integer,
    'weight': fields.Integer,
    'hp': fields.Integer,
    'attack': fields.Integer,
    'defense': fields.Integer,
    'special_attack': fields.Integer,
    'special_defense': fields.Integer,
    'speed': fields.Integer, 
})

postPokemon = api.model(name='PostPokemon', model={
    'name': fields.String,
    'height': fields.Integer,
    'weight': fields.Integer,
    'hp': fields.Integer,
    'attack': fields.Integer,
    'defense': fields.Integer,
    'special_attack': fields.Integer,
    'special_defense': fields.Integer,
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
            pokemon.special_attack = body['special_attack']
            pokemon.special_defense = body['special_defense']
            pokemon.speed = body['speed']
            db.session.commit()
        except:
            abort(500)
        
        return pokemon