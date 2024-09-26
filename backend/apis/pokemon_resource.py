from flask_restx import Namespace, Resource, fields, reqparse, abort
from core.database import db, Pokemons
from apis.models import pokemonModel, pokemonLocationModel, pokemonGameModel, pokemonAbilityModel, pokemonMoveModel, pgModel

namespace = Namespace('Pokemons', description='Recurso para pokemons')

pokemonDetails = namespace.inherit('PokemonDetails', pokemonModel, {
    'pokemonLocations': fields.List(fields.Nested(pokemonLocationModel)),
    'pokemonGames': fields.List(fields.Nested(pokemonGameModel)),
    'pokemonHabilities': fields.List(fields.Nested(pokemonAbilityModel)),
    'pokemonMoves': fields.List(fields.Nested(pokemonMoveModel))
})

pgPokemon = namespace.inherit('PgPokemon', pgModel, {
    'items': fields.List(fields.Nested(pokemonModel))
})

postPokemon = namespace.model(name='PostPokemon', model={
    'name': fields.String,
    'height': fields.Integer,
    'weight': fields.Integer,
    'hp': fields.Integer,
    'attack': fields.Integer,
    'defense': fields.Integer,
    'specialAttack': fields.Integer,
    'specialDefense': fields.Integer,
    'speed': fields.Integer, 
})

@namespace.route('')
class PokemonsResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)
    parser.add_argument('page', type=int)
    parser.add_argument('per_page', type=int)

    @namespace.expect(parser, validate=True)
    @namespace.marshal_with(pgPokemon)
    def get(self):
        args = self.parser.parse_args()
        query = db.session.query(Pokemons)

        if 'name' in args and args['name'] != None:
            query = query.filter(Pokemons.name.like('%'+args['name']+'%'))
        
        if 'page' in args and args['page'] != None:
            if 'per_page' in args and args['per_page'] != None:
                return query.paginate(page=int(args['page']), per_page=int(args['per_page']))
            
        return query.paginate(page=1, per_page=25)

        # query = query.order_by(Pokemons.codPokemon)

        # if 'offset' in args and args['offset'] != None:
        #     query = query.offset(args['offset'])

        # if 'limit' in args and args['limit'] != None:
        #     query = query.limit(args['limit'])
        # else:
        #     query = query.limit(12)


    @namespace.expect(postPokemon, validate=True)
    @namespace.marshal_with(pokemonModel)
    def post(self):
        body = namespace.payload

        newPokemon = Pokemons()
        newPokemon.name = body['name']
        newPokemon.height = body['height']
        newPokemon.weight = body['weight']
        newPokemon.hp = body['hp']
        newPokemon.attack = body['attack']
        newPokemon.defense = body['defense']
        newPokemon.specialAttack = body['specialAttack']
        newPokemon.specialDefense = body['specialDefense']
        newPokemon.speed = body['speed']
        newPokemon.spriteFrontDefault = body['spriteFrontDefault']
        newPokemon.spriteFrontShiny = body['spriteFrontShiny']

        db.session.add(newPokemon)
        db.session.commit()

        return newPokemon
    
@namespace.route('/details')
class PokemonsDetailsResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('codPokemon', type=int)

    @namespace.expect(parser)
    @namespace.marshal_with(pokemonDetails)
    def get(self):
        args = self.parser.parse_args()

        query = db.session.query(Pokemons)

        if 'codPokemon' in args and args['codPokemon'] != None:
            query = query.filter(Pokemons.codPokemon == args['codPokemon'])
        
        return query.first()
    
@namespace.route('/<int:codPokemon>')
class PokemonsResource(Resource):

    @namespace.marshal_with(pokemonDetails)
    def get(self, codPokemon: int):
        pokemon: Pokemons = db.session.query(Pokemons).get(codPokemon)
        if pokemon == None:
            abort(404, 'No se encuentra el pokemon buscado')

        return pokemon
    
    @namespace.expect(postPokemon, validate=True)
    @namespace.marshal_with(pokemonDetails)
    def put(self, codPokemon: int):
        body = namespace.payload

        pokemon: Pokemons = db.session.query(Pokemons).get(codPokemon)
        if pokemon == None:
            abort(404, 'No se encuentra el pokemon')

        try:
            pokemon.name = body['name']
            pokemon.height = body['height']
            pokemon.weight = body['weight']
            pokemon.hp = body['hp']
            pokemon.attack = body['attack']
            pokemon.defense = body['defense']
            pokemon.specialAttack = body['specialAttack']
            pokemon.specialDefense = body['specialDefense']
            pokemon.speed = body['speed']
            pokemon.spriteFrontDefault = body['spriteFrontDefault']
            pokemon.spriteFrontShiny = body['spriteFrontShiny']
            db.session.commit()
        except:
            abort(500)
        
        return pokemon