from core.database import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Habilities(db.Model):
    __tablename__ = "habilities"

    codHability = Column(name='cod_hability', type_=Integer, primary_key=True, autoincrement=True)
    name = Column(name='name', type_=String, nullable=False)
    description = Column(name='description', type_=String)

    pokemonsHability = relationship('PokemonHabilities', back_populates='hability')