from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()


from .location import Locations
from .pokemon import Pokemons
from .move import Moves
from .game import Games
from .hability import Habilities

from .pokemon_games import PokemonGames
from .pokemon_habilities import PokemonHabilities
from .pokemon_locations import PokemonLocations
from .pokemon_moves import PokemonMoves