from core.database import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class PokemonMoves(db.Model):
    __tablename__ = "pokemon_moves"

    codPokemonMove = Column('cod_pokemon_move', Integer, primary_key=True, autoincrement=True)
    pokemonCod = Column('pokemon_cod', Integer, ForeignKey('pokemons.cod_pokemon'), nullable=False)
    moveCod = Column('move_cod', Integer, ForeignKey('moves.cod_move'), nullable=False)

    pokemon = relationship('Pokemons', back_populates='pokemonMoves')
    move = relationship('Moves', back_populates='pokemonsMove')