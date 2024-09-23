from flask_restx import Namespace, Resource, fields, reqparse, abort
from core.database import db, Locations

api = Namespace('Locations', description='Recurso para locaciones')

baseLocation = api.model(name='BaseLocation', model={
    'codLocation': fields.Integer,
    'name': fields.String,
})

postLocation = api.model(name='PostLocation', model={
    'name': fields.String
})

@api.route('')
class LocationsResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)

    @api.expect(parser)
    @api.marshal_with(baseLocation, as_list=True)
    def get(self):
        args = self.parser.parse_args()
        
        #query = db.session.query(Locations).order_by(Locations.name)
        query = db.session.query(Locations)

        if 'name' in args and args['name'] != None:
            query = query.filter(Locations.name.like('%'+args['name']+'%'))

        return query.all()
    
    @api.expect(postLocation, validate=True)
    @api.marshal_with(baseLocation)
    def post(self):
        body = api.payload

        newLocation = Locations()
        newLocation.name = body['name']

        db.session.add(newLocation)
        db.session.commit()

        return newLocation

@api.route('/<int:codLocation>')
class LocationsResource(Resource):

    @api.marshal_with(baseLocation)
    def get(self, codLocation: int):
        location: Locations = db.session.query(Locations).get(codLocation)
        if location == None:
            abort(404, 'No se encuentra esa locación')
        return location
    
    @api.expect(postLocation, validate=True)
    @api.marshal_with(baseLocation)
    def put(self, codLocation: int):
        body = api.payload

        location: Locations = db.session.query(Locations).get(codLocation)
        if location == None:
            abort(404, 'No se encuentra esa locación')

        try:
            location.name = body['name']
            db.session.commit()
        except:
            abort(500)
            
        return location
