from core.database import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Moves(db.Model):
    __tablename__ = "moves"

    codMove = Column(name='cod_move', type_=Integer, primary_key=True, autoincrement=True)
    name = Column(name='name', type_=String, nullable=False)
    description = Column(name='description', type_=String, nullable=True)

    pokemonsMove = relationship('PokemonMoves', back_populates='move')