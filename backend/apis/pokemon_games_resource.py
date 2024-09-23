from flask_restx import Namespace, Resource, fields, reqparse, abort
from core.database import db, PokemonGames

api = Namespace('Pokemon Games', description='Recurso para pokemons y los juegos en donde aparece')

basePokemonGame = api.model(name='BasePokemonGame', model={
    'codPokemonGame': fields.Integer,
    'pokemonCod': fields.Integer,
    'gameCod': fields.Integer,
})

postPokemonGame = api.model(name='PostPokemonGame', model={
    'pokemonCod': fields.Integer,
    'gameCod': fields.Integer,
})

@api.route('')
class pokemonGameResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('pokemonCod', type=int)
    parser.add_argument('gameCod', type=int)

    @api.expect(parser)
    @api.marshal_with(basePokemonGame, as_list=True)
    def get(self):
        args = self.parser.parse_args()
        query = db.session.query(PokemonGames)

        if 'pokemonCod' in args and args['pokemonCod'] != None:
            query = query.filter(PokemonGames.pokemonCod == args['pokemonCod'])
        elif 'gameCod' in args and args['gameCod'] != None:
            query = query.filter(PokemonGames.gameCod == args['gameCod'])

        return query.all()
    
    @api.expect(postPokemonGame, validate=True)
    @api.marshal_with(basePokemonGame)
    def post(self):
        body = api.payload

        newPokemonGame = PokemonGames()
        newPokemonGame.pokemonCod = body['pokemonCod']
        newPokemonGame.gameCod = body['gameCod']

        db.session.add(newPokemonGame)
        db.session.commit()

        return newPokemonGame

@api.route('/<int:codePokemonGame>')
class GamesResource(Resource):

    @api.marshal_with(basePokemonGame)
    def get(self, codePokemonGame: int):
        pokemonGame: PokemonGames = db.session.query(PokemonGames).get(codePokemonGame)
        if pokemonGame == None:
            abort(404, 'No se encuentra el juego del pokemon')
        return pokemonGame
    
    @api.expect(postPokemonGame, validate=True)
    @api.marshal_with(basePokemonGame)
    def put(self, codePokemonGame: int):
        body = api.payload

        pokemonGame: PokemonGames = db.session.query(PokemonGames).get(codePokemonGame)
        if pokemonGame == None:
            abort(404, 'No se encuentran el juego del pokemon')

        try:
            pokemonGame.pokemonCod = body['pokemonCod']
            pokemonGame.pokemonCod = body['gameCod']
            db.session.commit()
        except:
            abort(500)
            
        return pokemonGame
