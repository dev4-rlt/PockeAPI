from core.database import db
from sqlalchemy import Column, Integer, ForeignKey

class PokemonLocations(db.Model):
    __tablename__ = "pokemon_locations"

    codPokemonLocation = Column('cod_pokemon_location', Integer, primary_key=True, autoincrement=True)
    pokemonCod = Column('pokemon_cod', Integer, ForeignKey('pokemons.cod_pokemon'), nullable=False)
    locationCod = Column('location_cod', Integer, ForeignKey('locations.cod_location'), nullable=False)