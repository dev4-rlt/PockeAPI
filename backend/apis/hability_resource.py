from flask_restx import Namespace, Resource, fields, reqparse, abort
from core.database import db, Habilities
from apis.models import habilityModel, pokemonHabilityModel

namespace = Namespace('Hability', description='Recurso para habilidades')

habilityDetails = namespace.inherit('HabilityDetails', habilityModel, {
    'pokemonsHability': fields.List(fields.Nested(pokemonHabilityModel))
})

postHability = namespace.model(name='PostHability', model={
    'name': fields.String,
    'description': fields.String,
})

@namespace.route('')
class HabilitiesResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)

    @namespace.expect(parser)
    @namespace.marshal_with(habilityDetails, as_list=True)
    def get(self):
        args = self.parser.parse_args()
        
        query = db.session.query(Habilities)

        if 'name' in args and args['name'] != None:
            query = query.filter(Habilities.name.like('%'+args['name']+'%'))

        return query.all()
    
    @namespace.expect(postHability, validate=True)
    @namespace.marshal_with(habilityDetails)
    def post(self):
        body = namespace.payload

        newHability = Habilities()
        newHability.name = body['name']
        
        if 'description' in body:
            newHability.description = body['description']

        db.session.add(newHability)
        db.session.commit()

        return newHability

@namespace.route('/<int:codHability>')
class HabilitysResource(Resource):

    @namespace.marshal_with(habilityDetails)
    def get(self, codHability: int):
        hability: Habilities = db.session.query(Habilities).get(codHability)
        if hability is None:
            abort(404, 'No se encuentra la habilidad')
        return hability
    
    @namespace.expect(postHability, validate=True)
    @namespace.marshal_with(habilityDetails)
    def put(self, codHability: int):
        body = namespace.payload

        hability: Habilities = db.session.query(Habilities).get(codHability)
        if hability == None:
            abort(404, 'No se encuentra la habilidad')

        try:
            hability.name = body['name']
            hability.name = body['description']
            db.session.commit()
        except:
            abort(500)
            
        return hability