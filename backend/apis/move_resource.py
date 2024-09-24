from flask_restx import Namespace, Resource, fields, reqparse, abort
from core.database import db, Moves
from apis.models import moveModel, pokemonMoveModel

namespace = Namespace('Moves', description='Recurso para movimientos')

moveDetails = namespace.inherit('MoveDetails', moveModel, {
    'pokemonsMove': fields.List(fields.Nested(pokemonMoveModel))
})

postMove = namespace.model(name='PostMove', model={
    'name': fields.String,
    'description': fields.String
})

@namespace.route('')
class MovesResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)

    @namespace.expect(parser)
    @namespace.marshal_with(moveDetails, as_list=True)
    def get(self):
        args = self.parser.parse_args()
        
        query = db.session.query(Moves)

        if 'name' in args and args['name'] != None:
            query = query.filter(Moves.name.like('%'+args['name']+'%'))

        return query.all()
    
    @namespace.expect(postMove, validate=True)
    @namespace.marshal_with(moveDetails)
    def post(self):
        body = namespace.payload

        newMove = Moves()
        newMove.name = body['name']
        
        if 'description' in body:
            newMove.description = body['description']

        db.session.add(newMove)
        db.session.commit()

        return newMove

@namespace.route('/<int:codHability>')
class HabilitysResource(Resource):

    @namespace.marshal_with(moveDetails)
    def get(self, codHability: int):
        hability: Moves = db.session.query(Moves).get(codHability)
        if hability is None:
            abort(404, 'No se encuentra el movimiento buscado')
        return hability
    
    @namespace.expect(postMove, validate=True)
    @namespace.marshal_with(moveDetails)
    def put(self, codMove: int):
        body = namespace.payload

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