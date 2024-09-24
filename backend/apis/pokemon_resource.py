from flask_restx import Namespace, Resource, fields, reqparse, abort
from core.database import db, Pokemons
from apis.models import pokemonModel, pokemonLocationModel, pokemonGameModel, pokemonAbilityModel, pokemonMoveModel

namespace = Namespace('Pokemons', description='Recurso para pokemons')

pokemonDetails = namespace.inherit('PokemonDetails', pokemonModel, {
    'pokemonLocations': fields.List(fields.Nested(pokemonLocationModel)),
    'pokemonGames': fields.List(fields.Nested(pokemonGameModel)),
    'pokemonHabilities': fields.List(fields.Nested(pokemonAbilityModel)),
    'pokemonMoves': fields.List(fields.Nested(pokemonMoveModel))
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

@namespace.route('')
class PokemonsResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)

    @namespace.expect(parser)
    @namespace.marshal_with(pokemonDetails, as_list=True)
    def get(self):
        args = self.parser.parse_args()

        query = db.session.query(Pokemons)

        if 'name' in args and args['name'] != None:
            query = query.filter(Pokemons.name.like('%'+args['name']+'%'))

        return query.all()

    @namespace.expect(postPokemon, validate=True)
    @namespace.marshal_with(pokemonDetails)
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
            db.session.commit()
        except:
            abort(500)
        
        return pokemon