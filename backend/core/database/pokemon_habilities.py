from core.database import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class PokemonHabilities(db.Model):
    __tablename__ = "pokemon_habilities"

    codPokemonAbility = Column('cod_pokemon_hability', Integer, primary_key=True, autoincrement=True)
    pokemonCod = Column('pokemon_cod', Integer, ForeignKey('pokemons.cod_pokemon'), nullable=False)
    abilityCod = Column('hability_cod', Integer, ForeignKey('habilities.cod_hability'), nullable=False)

    pokemon = relationship('Pokemons', back_populates='pokemonHabilities')
    ability = relationship('Habilities', back_populates='pokemonsAbility')