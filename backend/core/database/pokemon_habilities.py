from core.database import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class PokemonHabilities(db.Model):
    __tablename__ = "pokemon_habilities"

    codPokemonHability = Column('cod_pokemon_hability', Integer, primary_key=True, autoincrement=True)
    pokemonCod = Column('pokemon_cod', Integer, ForeignKey('pokemons.cod_pokemon'), nullable=False)
    habilityCod = Column('hability_cod', Integer, ForeignKey('habilities.cod_hability'), nullable=False)

    pokemon = relationship('Pokemons', back_populates='pokemonHabilities')
    hability = relationship('Habilities', back_populates='pokemonsHability')