from flask_restx import Namespace, Resource, fields, reqparse, abort
from core.database import db, PokemonHabilities

api = Namespace('Pokemon Habilities', description='Recurso para pokemons y sus habilidades')

basePokemonHability = api.model(name='BasePokemonHability', model={
    'codPokemonHability': fields.Integer,
    'pokemonCod': fields.Integer,
    'habilityCod': fields.Integer,
})

postPokemonHability = api.model(name='PostPokemonHability', model={
    'pokemonCod': fields.Integer,
    'habilityCod': fields.Integer,
})

@api.route('')
class PokemonHabilityResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('pokemonCod', type=int)
    parser.add_argument('habilityCod', type=int)

    @api.expect(parser)
    @api.marshal_with(basePokemonHability, as_list=True)
    def get(self):
        args = self.parser.parse_args()
        query = db.session.query(PokemonHabilities)

        if 'pokemonCod' in args and args['pokemonCod'] != None:
            query = query.filter(PokemonHabilities.pokemonCod == args['pokemonCod'])
        elif 'habilityCod' in args and args['habilityCod'] != None:
            query = query.filter(PokemonHabilities.habilityCod == args['habilityCod'])

        return query.all()
    
    @api.expect(postPokemonHability, validate=True)
    @api.marshal_with(basePokemonHability)
    def post(self):
        body = api.payload

        newPokemonHability = PokemonHabilities()
        newPokemonHability.pokemonCod = body['pokemonCod']
        newPokemonHability.habilityCod = body['habilityCod']

        db.session.add(newPokemonHability)
        db.session.commit()

        return newPokemonHability

@api.route('/<int:codPokemonHability>')
class GamesResource(Resource):

    @api.marshal_with(basePokemonHability)
    def get(self, codPokemonHability: int):
        pokemonHability: PokemonHabilities = db.session.query(PokemonHabilities).get(codPokemonHability)
        if pokemonHability == None:
            abort(404, 'No se encuentra la habilidad del pokemon')
        return pokemonHability
    
    @api.expect(postPokemonHability, validate=True)
    @api.marshal_with(basePokemonHability)
    def put(self, codPokemonHability: int):
        body = api.payload

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
