from core.database import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Games(db.Model):
    __tablename__ = "games"

    codGame = Column(name='cod_game', type_=Integer, primary_key=True, autoincrement=True)
    name = Column(name='name', type_=String, nullable=False)

    pokemonsGame = relationship('PokemonGames', back_populates='game')