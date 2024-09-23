from flask_restx import Namespace, Resource, fields, reqparse, abort
from core.database import db, Moves

api = Namespace('Moves', description='Recurso para movimientos')

baseMove = api.model(name='BaseMove', model={
    'codMove': fields.Integer,
    'name': fields.String,
    'description': fields.String,
})

postMove = api.model(name='PostMove', model={
    'name': fields.String,
    'description': fields.String
})

@api.route('')
class MovesResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)

    @api.expect(parser)
    @api.marshal_with(baseMove, as_list=True)
    def get(self):
        args = self.parser.parse_args()
        
        query = db.session.query(Moves)

        if 'name' in args and args['name'] != None:
            query = query.filter(Moves.name.like('%'+args['name']+'%'))

        return query.all()
    
    @api.expect(postMove, validate=True)
    @api.marshal_with(baseMove)
    def post(self):
        body = api.payload

        newMove = Moves()
        newMove.name = body['name']
        
        if 'description' in body:
            newMove.description = body['description']

        db.session.add(newMove)
        db.session.commit()

        return newMove

@api.route('/<int:codHability>')
class HabilitysResource(Resource):

    @api.marshal_with(baseMove)
    def get(self, codHability: int):
        hability: Moves = db.session.query(Moves).get(codHability)
        if hability is None:
            abort(404, 'No se encuentra el movimiento')
        return hability
    
    @api.expect(postMove, validate=True)
    @api.marshal_with(baseMove)
    def put(self, codMove: int):
        body = api.payload

        move: Moves = db.session.query(Moves).get(codMove)
        if move == None:
            abort(404, 'No se encuentra el movimiento')

        try:
            move.name = body['name']
            move.name = body['description']
            db.session.commit()
        except:
            abort(500)
            
        return move