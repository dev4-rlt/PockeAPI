from flask_restx import Namespace, Resource, fields, reqparse, abort
from core.database import db, PokemonMoves
from apis.models import pokemonMoveModel

namespace = Namespace('Pokemon Moves', description='Recurso para pokemons y sus movimientos')

postpokemonMove = namespace.model(name='PostPokemonMove', model={
    'pokemonCod': fields.Integer,
    'moveCod': fields.Integer,
})

@namespace.route('')
class pokemonMoveResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('pokemonCod', type=int)
    parser.add_argument('moveCod', type=int)

    @namespace.expect(parser)
    @namespace.marshal_with(pokemonMoveModel, as_list=True)
    def get(self):
        args = self.parser.parse_args()
        query = db.session.query(PokemonMoves)

        if 'pokemonCod' in args and args['pokemonCod'] != None:
            query = query.filter(PokemonMoves.pokemonCod == args['pokemonCod'])
        elif 'moveCod' in args and args['moveCod'] != None:
            query = query.filter(PokemonMoves.moveCod == args['moveCod'])

        return query.all()
    
    @namespace.expect(postpokemonMove, validate=True)
    @namespace.marshal_with(pokemonMoveModel)
    def post(self):
        body = namespace.payload

        newPokemonMove = PokemonMoves()
        newPokemonMove.pokemonCod = body['pokemonCod']
        newPokemonMove.moveCod = body['moveCod']

        db.session.add(newPokemonMove)
        db.session.commit()

        return newPokemonMove

@namespace.route('/<int:codePokemonMove>')
class GamesResource(Resource):

    @namespace.marshal_with(pokemonMoveModel)
    def get(self, codePokemonMove: int):
        pokemonMove: PokemonMoves = db.session.query(PokemonMoves).get(codePokemonMove)
        if pokemonMove == None:
            abort(404, 'No se encuentra el movimiento del pokemon que se busca')
        return pokemonMove
    
    @namespace.expect(postpokemonMove, validate=True)
    @namespace.marshal_with(pokemonMoveModel)
    def put(self, codePokemonMove: int):
        body = namespace.payload

        pokemonMove: PokemonMoves = db.session.query(PokemonMoves).get(codePokemonMove)
        if pokemonMove == None:
            abort(404, 'No se encuentran el movimiento del pokemon')

        try:
            pokemonMove.pokemonCod = body['pokemonCod']
            pokemonMove.moveCod = body['moveCod']
            db.session.commit()
        except:
            abort(500)
            
        return pokemonMove
