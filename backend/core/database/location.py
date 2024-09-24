from core.database import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Locations(db.Model):
    __tablename__ = "locations"

    codLocation = Column(name='cod_location', type_=Integer, primary_key=True, autoincrement=True)
    name = Column(name='name', type_=String, nullable=False)

    pokemonsLocation = relationship('PokemonLocations', back_populates='location')