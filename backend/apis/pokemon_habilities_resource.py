from flask_restx import Namespace, Resource, fields, reqparse, abort
from core.database import db, PokemonHabilities
from apis.models import pokemonHabilityModel

namespace = Namespace('Pokemon Habilities', description='Recurso para pokemons y sus habilidades')

postPokemonHability = namespace.model(name='PostPokemonHability', model={
    'pokemonCod': fields.Integer,
    'habilityCod': fields.Integer,
})

@namespace.route('')
class PokemonHabilityResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('pokemonCod', type=int)
    parser.add_argument('habilityCod', type=int)

    @namespace.expect(parser)
    @namespace.marshal_with(pokemonHabilityModel, as_list=True)
    def get(self):
        args = self.parser.parse_args()
        query = db.session.query(PokemonHabilities)

        if 'pokemonCod' in args and args['pokemonCod'] != None:
            query = query.filter(PokemonHabilities.pokemonCod == args['pokemonCod'])
        elif 'habilityCod' in args and args['habilityCod'] != None:
            query = query.filter(PokemonHabilities.habilityCod == args['habilityCod'])

        return query.all()
    
    @namespace.expect(postPokemonHability, validate=True)
    @namespace.marshal_with(pokemonHabilityModel)
    def post(self):
        body = namespace.payload

        newPokemonHability = PokemonHabilities()
        newPokemonHability.pokemonCod = body['pokemonCod']
        newPokemonHability.habilityCod = body['habilityCod']

        db.session.add(newPokemonHability)
        db.session.commit()

        return newPokemonHability

@namespace.route('/<int:codPokemonHability>')
class GamesResource(Resource):

    @namespace.marshal_with(pokemonHabilityModel)
    def get(self, codPokemonHability: int):
        pokemonHability: PokemonHabilities = db.session.query(PokemonHabilities).get(codPokemonHability)
        if pokemonHability == None:
            abort(404, 'No se encuentra la habilidad del pokemon')
        return pokemonHability
    
    @namespace.expect(postPokemonHability, validate=True)
    @namespace.marshal_with(pokemonHabilityModel)
    def put(self, codPokemonHability: int):
        body = namespace.payload

        pokemonHability: PokemonHabilities = db.session.query(PokemonHabilities).get(codPokemonHability)
        if pokemonHability == None:
            abort(404, 'No se encuentran la habilidad del pokemon')

        try:
            pokemonHability.pokemonCod = body['pokemonCod']
            pokemonHability.habilityCod = body['habilityCod']
            db.session.commit()
        except:
            abort(500)
            
        return pokemonHability
