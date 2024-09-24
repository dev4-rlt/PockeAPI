from flask_restx import Namespace, Resource, fields, reqparse, abort
from core.database import db, PokemonHabilities
from apis.models import pokemonAbilityModel

namespace = Namespace('Pokemon Habilities', description='Recurso para pokemons y sus habilidades')

postPokemonAbility = namespace.model(name='PostPokemonAbility', model={
    'pokemonCod': fields.Integer,
    'abilityCod': fields.Integer,
})

@namespace.route('')
class PokemonAbilityResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('pokemonCod', type=int)
    parser.add_argument('abilityCod', type=int)

    @namespace.expect(parser)
    @namespace.marshal_with(pokemonAbilityModel, as_list=True)
    def get(self):
        args = self.parser.parse_args()
        query = db.session.query(PokemonHabilities)

        if 'pokemonCod' in args and args['pokemonCod'] != None:
            query = query.filter(PokemonHabilities.pokemonCod == args['pokemonCod'])
        elif 'abilityCod' in args and args['abilityCod'] != None:
            query = query.filter(PokemonHabilities.abilityCod == args['abilityCod'])

        return query.all()
    
    @namespace.expect(postPokemonAbility, validate=True)
    @namespace.marshal_with(pokemonAbilityModel)
    def post(self):
        body = namespace.payload

        newPokemonAbility = PokemonHabilities()
        newPokemonAbility.pokemonCod = body['pokemonCod']
        newPokemonAbility.abilityCod = body['abilityCod']

        db.session.add(newPokemonAbility)
        db.session.commit()

        return newPokemonAbility

@namespace.route('/<int:codPokemonAbility>')
class GamesResource(Resource):

    @namespace.marshal_with(pokemonAbilityModel)
    def get(self, codPokemonAbility: int):
        pokemonAbility: PokemonHabilities = db.session.query(PokemonHabilities).get(codPokemonAbility)
        if pokemonAbility == None:
            abort(404, 'No se encuentra la habilidad del pokemon que se busca')
        return pokemonAbility
    
    @namespace.expect(postPokemonAbility, validate=True)
    @namespace.marshal_with(pokemonAbilityModel)
    def put(self, codPokemonAbility: int):
        body = namespace.payload

        pokemonAbility: PokemonHabilities = db.session.query(PokemonHabilities).get(codPokemonAbility)
        if pokemonAbility == None:
            abort(404, 'No se encuentra la habilidad del pokemon')

        try:
            pokemonAbility.pokemonCod = body['pokemonCod']
            pokemonAbility.abilityCod = body['abilityCod']
            db.session.commit()
        except:
            abort(500)
            
        return pokemonAbility
