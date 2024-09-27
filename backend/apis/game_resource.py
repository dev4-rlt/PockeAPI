from flask_restx import Namespace, Resource, fields, reqparse, abort
from core.database import db, Games
from apis.models import gameModel, pokemonGameModel, postGame

namespace = Namespace('Games', description='Recurso para juegos')

gameDetails = namespace.inherit('GameDetails', gameModel, {
    'pokemonsGame': fields.List(fields.Nested(pokemonGameModel))
})

@namespace.route('')
class GamesResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)

    @namespace.expect(parser)
    @namespace.marshal_with(gameDetails, as_list=True)
    def get(self):
        args = self.parser.parse_args()
        query = db.session.query(Games)

        if 'name' in args and args['name'] != None:
            query = query.filter(Games.name.like('%'+args['name']+'%'))

        return query.all()
    
    @namespace.expect(postGame, validate=True)
    @namespace.marshal_with(gameDetails)
    def post(self):
        body = namespace.payload

        newGame = Games()
        newGame.name = body['name']

        db.session.add(newGame)
        db.session.commit()

        return newGame

@namespace.route('/<int:codGame>')
class GamesResource(Resource):

    @namespace.marshal_with(gameDetails)
    def get(self, codGame: int):
        game: Games = db.session.query(Games).get(codGame)
        if game == None:
            abort(404, 'No se encuentra el juego buscado')
        return game
    
    @namespace.expect(postGame, validate=True)
    @namespace.marshal_with(gameDetails)
    def put(self, codGame: int):
        body = namespace.payload

        game: Games = db.session.query(Games).get(codGame)
        if game == None:
            abort(404, 'No se encuentra esa locación')

        try:
            game.name = body['name']
            db.session.commit()
        except:
            abort(500)
            
        return game
