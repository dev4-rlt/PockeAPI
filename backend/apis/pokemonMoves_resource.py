from flask_restx import Namespace, Resource, fields, reqparse, abort
from core.database import db, PokemonMoves

api = Namespace('Pokemon Moves', description='Recurso para pokemons y sus movimientos')

basePokemonMove = api.model(name='BasePokemonMove', model={
    'codPokemonMove': fields.Integer,
    'pokemonCod': fields.Integer,
    'moveCod': fields.Integer,
})

postpokemonMove = api.model(name='PostPokemonMove', model={
    'pokemonCod': fields.Integer,
    'moveCod': fields.Integer,
})

@api.route('')
class pokemonMoveResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('pokemonCod', type=int)
    parser.add_argument('moveCod', type=int)

    @api.expect(parser)
    @api.marshal_with(basePokemonMove, as_list=True)
    def get(self):
        args = self.parser.parse_args()
        query = db.session.query(PokemonMoves)

        if 'pokemonCod' in args and args['pokemonCod'] != None:
            query = query.filter(PokemonMoves.pokemonCod == args['pokemonCod'])
        elif 'moveCod' in args and args['moveCod'] != None:
            query = query.filter(PokemonMoves.moveCod == args['moveCod'])

        return query.all()
    
    @api.expect(postpokemonMove, validate=True)
    @api.marshal_with(basePokemonMove)
    def post(self):
        body = api.payload

        newPokemonMove = PokemonMoves()
        newPokemonMove.pokemonCod = body['pokemonCod']
        newPokemonMove.moveCod = body['moveCod']

        db.session.add(newPokemonMove)
        db.session.commit()

        return newPokemonMove

@api.route('/<int:codePokemonMove>')
class GamesResource(Resource):

    @api.marshal_with(basePokemonMove)
    def get(self, codePokemonMove: int):
        pokemonMove: PokemonMoves = db.session.query(PokemonMoves).get(codePokemonMove)
        if pokemonMove == None:
            abort(404, 'No se encuentra el movimiento del pokemon')
        return pokemonMove
    
    @api.expect(postpokemonMove, validate=True)
    @api.marshal_with(basePokemonMove)
    def put(self, codePokemonMove: int):
        body = api.payload

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
