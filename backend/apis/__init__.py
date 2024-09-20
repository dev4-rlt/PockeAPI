from flask_restx import Api

from .pokemon_resource import api as pokemones

api = Api(
    title='Practica pokemon',
    version='1.0',
)

api.add_namespace(pokemones, path='/pokemons')