from core.database import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Pokemons(db.Model):
    __tablename__ = "pokemons"

    codPokemon = Column('cod_pokemon', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    height = Column('height', Integer, nullable=False)
    weight = Column('weight', Integer, nullable=False)
    hp = Column('hp', Integer, nullable=False)
    attack = Column('attack', Integer, nullable=False)
    defense = Column('defense', Integer, nullable=False)
    specialAttack = Column('special_attack', Integer, nullable=False)
    specialDefense = Column('special_defense', Integer, nullable=False)
    speed = Column('speed', Integer, nullable=False)
    spriteFrontDefault = Column('sprite_front_default', String)
    spriteFrontShiny = Column('sprite_front_shiny', String)

    pokemonLocations = relationship('PokemonLocations', back_populates='pokemon')
    pokemonHabilities = relationship('PokemonHabilities', back_populates='pokemon')
    pokemonMoves = relationship('PokemonMoves', back_populates='pokemon')
    pokemonGames = relationship('PokemonGames', back_populates='pokemon')