from flask_restx import Namespace, Resource, fields, reqparse
import requests
import json

api = Namespace('Pokemons', description='Recurso para pokemons')

basePokemon = api.model(name='BasePokemon', model={
    'name': fields.String,
    'url': fields.String,
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
    def get(self):
        args = self.parser.parse_args()

        req = requests.get('https://pokeapi.co/api/v2/pokemon', params=args)
        data = json.loads(req.text)
        return data
    
# @api.route('/<string:url>')
# class PokemonsResource(Resource):
#     @api.marshal_with(pokemonPaged)
#     def get(self, url: str):
#         print(url)
#         return pokemonPaged.text