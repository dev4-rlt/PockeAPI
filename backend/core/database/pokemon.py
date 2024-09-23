from core.database import db
from sqlalchemy import Column, Integer, String

class Pokemons(db.Model):
    __tablename__ = "pokemons"

    codPokemon = Column(name='cod_pokemon', type_=Integer, primary_key=True, autoincrement=True)
    name = Column(name='name', type_=String, nullable=False)
    height = Column(name='height', type_=Integer, nullable=False)
    weight = Column(name='weight', type_=Integer, nullable=False)
    hp = Column(name='hp', type_=Integer, nullable=False)
    attack = Column(name='attack', type_=Integer, nullable=False)
    defense = Column(name='defense', type_=Integer, nullable=False)
    special_attack = Column(name='special_attack', type_=Integer, nullable=False)
    special_defense = Column(name='special_defense', type_=Integer, nullable=False)
    speed = Column(name='speed', type_=Integer, nullable=False)