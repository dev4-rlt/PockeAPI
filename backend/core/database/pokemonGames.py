from core.database import db
from sqlalchemy import Column, Integer, ForeignKey

class PokemonGames(db.Model):
    __tablename__ = "pokemon_games"

    codPokemonGame = Column('cod_pokemon_game', Integer, primary_key=True, autoincrement=True)
    pokemonCod = Column('pokemon_cod', Integer, ForeignKey('pokemons.cod_pokemon'), nullable=False)
    gameCod = Column('game_cod', Integer, ForeignKey('games.cod_game'), nullable=False)