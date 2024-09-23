from flask_restx import Namespace, Resource, fields, reqparse, abort
from core.database import db, Habilities

api = Namespace('Hability', description='Recurso para habilidades')

baseHability = api.model(name='BaseHability', model={
    'codHability': fields.Integer,
    'name': fields.String,
    'description': fields.String,
})

postHability = api.model(name='PostHability', model={
    'name': fields.String,
    'description': fields.String,
})

@api.route('')
class HabilitiesResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)

    @api.expect(parser)
    @api.marshal_with(baseHability, as_list=True)
    def get(self):
        args = self.parser.parse_args()
        
        query = db.session.query(Habilities)

        if 'name' in args and args['name'] != None:
            query = query.filter(Habilities.name.like('%'+args['name']+'%'))

        return query.all()
    
    @api.expect(postHability, validate=True)
    @api.marshal_with(baseHability)
    def post(self):
        body = api.payload

        newHability = Habilities()
        newHability.name = body['name']
        
        if 'description' in body:
            newHability.description = body['description']

        db.session.add(newHability)
        db.session.commit()

        return newHability

@api.route('/<int:codHability>')
class HabilitysResource(Resource):

    @api.marshal_with(baseHability)
    def get(self, codHability: int):
        hability: Habilities = db.session.query(Habilities).get(codHability)
        if hability is None:
            abort(404, 'No se encuentra la habilidad')
        return hability
    
    @api.expect(postHability, validate=True)
    @api.marshal_with(baseHability)
    def put(self, codHability: int):
        body = api.payload

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