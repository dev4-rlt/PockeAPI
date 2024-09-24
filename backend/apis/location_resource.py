from flask_restx import Namespace, Resource, fields, reqparse, abort
from core.database import db, Locations
from apis.models import locationModel, pokemonLocationModel

namespace = Namespace('Locations', description='Recurso para locaciones')

locationDetails = namespace.inherit('LocationDetails', locationModel, {
    'pokemonsLocation': fields.List(fields.Nested(pokemonLocationModel))
})

postLocation = namespace.model(name='PostLocation', model={
    'name': fields.String
})

@namespace.route('')
class LocationsResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)

    @namespace.expect(parser)
    @namespace.marshal_with(locationDetails, as_list=True)
    def get(self):
        args = self.parser.parse_args()
        
        #query = db.session.query(Locations).order_by(Locations.name)
        query = db.session.query(Locations)

        if 'name' in args and args['name'] != None:
            query = query.filter(Locations.name.like('%'+args['name']+'%'))

        return query.all()
    
    @namespace.expect(postLocation, validate=True)
    @namespace.marshal_with(locationDetails)
    def post(self):
        body = namespace.payload

        newLocation = Locations()
        newLocation.name = body['name']

        db.session.add(newLocation)
        db.session.commit()

        return newLocation

@namespace.route('/<int:codLocation>')
class LocationsResource(Resource):

    @namespace.marshal_with(locationDetails)
    def get(self, codLocation: int):
        location: Locations = db.session.query(Locations).get(codLocation)
        if location == None:
            abort(404, 'No se encuentra esa locación')
        return location
    
    @namespace.expect(postLocation, validate=True)
    @namespace.marshal_with(locationDetails)
    def put(self, codLocation: int):
        body = namespace.payload

        location: Locations = db.session.query(Locations).get(codLocation)
        if location == None:
            abort(404, 'No se encuentra esa locación')

        try:
            location.name = body['name']
            db.session.commit()
        except:
            abort(500)
            
        return location
