from flask_restx import Api

from .pokemon_resource import api as pokemones
from .location_resource import api as locations
from .game_resource import api as games
from .hability_resource import api as habilities
from .move_resource import api as moves
from .pokemon_habilities_resource import api as pokemonHabilities
from .pokemonMoves_resource import api as pokemonMoves
from .pokemon_locations_resource import api as pokemonLocations
from .pokemon_games_resource import api as pokemonGames

api = Api(
    title='Practica pokemon',
    version='1.0',
)

api.add_namespace(pokemones, path='/pokemons')
api.add_namespace(locations, path='/locations')
api.add_namespace(games, path='/games')
api.add_namespace(habilities, path='/habilities')
api.add_namespace(moves, path='/moves')
api.add_namespace(pokemonHabilities, path='/pokemon-habilities')
api.add_namespace(pokemonMoves, path='/pokemon-moves')
api.add_namespace(pokemonLocations, path='/pokemon-locations')
api.add_namespace(pokemonGames, path='/pokemon-games')