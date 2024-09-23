from flask_restx import Namespace, Resource, fields, reqparse, abort
from core.database import db, PokemonLocations

api = Namespace('Pokemon Locations', description='Recurso para pokemons y sus locaciones')

basePokemonLocation = api.model(name='BasePokemonLocation', model={
    'codPokemonLocation': fields.Integer,
    'pokemonCod': fields.Integer,
    'locationCod': fields.Integer,
})

postPokemonLocation = api.model(name='PostPokemonLocation', model={
    'pokemonCod': fields.Integer,
    'locationCod': fields.Integer,
})

@api.route('')
class pokemonLocationResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('pokemonCod', type=int)
    parser.add_argument('locationCod', type=int)

    @api.expect(parser)
    @api.marshal_with(basePokemonLocation, as_list=True)
    def get(self):
        args = self.parser.parse_args()
        query = db.session.query(PokemonLocations)

        if 'pokemonCod' in args and args['pokemonCod'] != None:
            query = query.filter(PokemonLocations.pokemonCod == args['pokemonCod'])
        elif 'locationCod' in args and args['locationCod'] != None:
            query = query.filter(PokemonLocations.locationCod == args['locationCod'])

        return query.all()
    
    @api.expect(postPokemonLocation, validate=True)
    @api.marshal_with(basePokemonLocation)
    def post(self):
        body = api.payload

        newPokemonLocation = PokemonLocations()
        newPokemonLocation.pokemonCod = body['pokemonCod']
        newPokemonLocation.locationCod = body['locationCod']

        db.session.add(newPokemonLocation)
        db.session.commit()

        return newPokemonLocation

@api.route('/<int:codePokemonLocation>')
class GamesResource(Resource):

    @api.marshal_with(basePokemonLocation)
    def get(self, codePokemonLocation: int):
        pokemonLocation: PokemonLocations = db.session.query(PokemonLocations).get(codePokemonLocation)
        if pokemonLocation == None:
            abort(404, 'No se encuentra el movimiento del pokemon')
        return pokemonLocation
    
    @api.expect(postPokemonLocation, validate=True)
    @api.marshal_with(basePokemonLocation)
    def put(self, codePokemonLocation: int):
        body = api.payload

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
