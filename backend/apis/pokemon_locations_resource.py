from flask_restx import Namespace, Resource, fields, reqparse, abort
from core.database import db, PokemonLocations
from apis.models import pokemonLocationModel

namespace = Namespace('Pokemon Locations', description='Recurso para pokemons y sus locaciones')

postPokemonLocation = namespace.model(name='PostPokemonLocation', model={
    'pokemonCod': fields.Integer,
    'locationCod': fields.Integer,
})

@namespace.route('')
class pokemonLocationResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('pokemonCod', type=int)
    parser.add_argument('locationCod', type=int)

    @namespace.expect(parser)
    @namespace.marshal_with(pokemonLocationModel, as_list=True)
    def get(self):
        args = self.parser.parse_args()
        query = db.session.query(PokemonLocations)

        if 'pokemonCod' in args and args['pokemonCod'] != None:
            query = query.filter(PokemonLocations.pokemonCod == args['pokemonCod'])
        elif 'locationCod' in args and args['locationCod'] != None:
            query = query.filter(PokemonLocations.locationCod == args['locationCod'])

        return query.all()
    
    @namespace.expect(postPokemonLocation, validate=True)
    @namespace.marshal_with(pokemonLocationModel)
    def post(self):
        body = namespace.payload

        newPokemonLocation = PokemonLocations()
        newPokemonLocation.pokemonCod = body['pokemonCod']
        newPokemonLocation.locationCod = body['locationCod']

        db.session.add(newPokemonLocation)
        db.session.commit()

        return newPokemonLocation

@namespace.route('/<int:codePokemonLocation>')
class GamesResource(Resource):

    @namespace.marshal_with(pokemonLocationModel)
    def get(self, codePokemonLocation: int):
        pokemonLocation: PokemonLocations = db.session.query(PokemonLocations).get(codePokemonLocation)
        if pokemonLocation == None:
            abort(404, 'No se encuentra el movimiento del pokemon')
        return pokemonLocation
    
    @namespace.expect(postPokemonLocation, validate=True)
    @namespace.marshal_with(pokemonLocationModel)
    def put(self, codePokemonLocation: int):
        body = namespace.payload

        pokemonLocation: PokemonLocations = db.session.query(PokemonLocations).get(codePokemonLocation)
        if pokemonLocation == None:
            abort(404, 'No se encuentran el movimiento del pokemon')

        try:
            pokemonLocation.pokemonCod = body['pokemonCod']
            pokemonLocation.locationCod = body['locationCod']
            db.session.commit()
        except:
            abort(500)
            
        return pokemonLocation
