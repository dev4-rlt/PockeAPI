from flask_restx import Namespace, Resource, fields, reqparse, abort
from core.database import db, Games

api = Namespace('Games', description='Recurso para juegos')

baseGame = api.model(name='BaseGame', model={
    'codGame': fields.Integer,
    'name': fields.String,
})

postGame = api.model(name='PostGame', model={
    'name': fields.String,
})

@api.route('')
class GamesResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)

    @api.expect(parser)
    @api.marshal_with(baseGame, as_list=True)
    def get(self):
        args = self.parser.parse_args()
        query = db.session.query(Games)

        if 'name' in args and args['name'] != None:
            query = query.filter(Games.name.like('%'+args['name']+'%'))

        return query.all()
    
    @api.expect(postGame, validate=True)
    @api.marshal_with(baseGame)
    def post(self):
        body = api.payload

        newGame = Games()
        newGame.name = body['name']

        db.session.add(newGame)
        db.session.commit()

        return newGame

@api.route('/<int:codGame>')
class GamesResource(Resource):

    @api.marshal_with(baseGame)
    def get(self, codGame: int):
        game: Games = db.session.query(Games).get(codGame)
        if game == None:
            abort(404, 'No se encuentra el juego')
        return game
    
    @api.expect(postGame, validate=True)
    @api.marshal_with(baseGame)
    def put(self, codGame: int):
        body = api.payload

        game: Games = db.session.query(Games).get(codGame)
        if game == None:
            abort(404, 'No se encuentra esa locación')

        try:
            game.name = body['name']
            db.session.commit()
        except:
            abort(500)
            
        return game
