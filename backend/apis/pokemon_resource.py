from flask_restx import Namespace, Resource, fields, reqparse
import requests
import json
import sqlalchemy

api = Namespace('Pokemons', description='Recurso para pokemons')

print(sqlalchemy.__version__)

basePokemon = api.model(name='BasePokemon', model={
    'id': fields.Integer,
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

pagedPokemons = api.model(name='PagedPokemons', model={
    'count': fields.String,
    'next': fields.String,
    'previous': fields.String,
    'results': fields.List(fields.Nested(basePokemon))
})

@api.route('')
class PokemonsResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('limit', type=int)
    parser.add_argument('offset', type=int)

    @api.expect(parser)
    @api.marshal_with(pagedPokemons)
    def get(self):#get pokemons
        args = self.parser.parse_args()

        req = requests.get('https://pokeapi.co/api/v2/pokemon', params=args)
        data = json.loads(req.text)
        return data
    
# @api.route('/details/<string:url>')#get pokemon details
# class PokemonsResource(Resource):
#     @api.marshal_with(pokemonPaged)
#     def get(self, url: str):
#         print(url)
#         return pokemonPaged.text