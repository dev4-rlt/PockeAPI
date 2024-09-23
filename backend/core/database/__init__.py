from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()


from .location import Locations
from .pokemon import Pokemons
from .move import Moves
from .game import Games
from .hability import Habilities

from .pokemonGames import PokemonGames
from .pokemonHabilities import PokemonHabilities
from .pokemonLocations import PokemonLocations
from .pokemonMoves import PokemonMoves