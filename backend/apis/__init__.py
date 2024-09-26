from flask_restx import Api

api = Api(
    title='Practica pokemon',
    version='1.0',
)

from .pokemon_resource import namespace as pokemones
from .location_resource import namespace as locations
from .game_resource import namespace as games
from .ability_resource import namespace as habilities
from .move_resource import namespace as moves
from .pokemon_habilities_resource import namespace as pokemonHabilities
from .pokemonMoves_resource import namespace as pokemonMoves
from .pokemon_locations_resource import namespace as pokemonLocations
from .pokemon_games_resource import namespace as pokemonGames
from .migraciones_resource import namespace as migraciones

from .user_resource import namespace as users

# Pokemons and details
api.add_namespace(pokemones, path='/pokemons')
api.add_namespace(locations, path='/locations')
api.add_namespace(games, path='/games')
api.add_namespace(habilities, path='/habilities')
api.add_namespace(moves, path='/moves')
api.add_namespace(pokemonHabilities, path='/pokemon-habilities')
api.add_namespace(pokemonMoves, path='/pokemon-moves')
api.add_namespace(pokemonLocations, path='/pokemon-locations')
api.add_namespace(pokemonGames, path='/pokemon-games')

# Users
api.add_namespace(users, path='/users')

# Migraciones
api.add_namespace(migraciones, path='/migracion')