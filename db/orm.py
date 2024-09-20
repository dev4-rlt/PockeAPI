from typing Optional
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Pokemon(Base):
    __tablename__ = 'pokemon'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    height: Mapped[int] = mapped_column(int)
    weight: Mapped[int] = mapped_column(int)
    hp: Mapped[int] = mapped_column(int)
    attack: Mapped[int] = mapped_column(int)
    defense: Mapped[int] = mapped_column(int)
    special_attack: Mapped[int] = mapped_column(int)
    special_defense: Mapped[int] = mapped_column(int)
    speed: Mapped[int] = mapped_column(int)

class Hability(Base):
    __tablename__ = 'hability'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    description: Mapped[Optional[str]]

class Move(Base):
    __tablename__ = 'move'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    description: Mapped[Optional[str]]

class Location(Base):
    __tablename__ = 'location'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))

class Game(Base):
    __tablename__ = 'game'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))

# ======= Tablas pendientes =======
# pokemon_hability
# pokemon_move
# pokemon_location
# pokemon_game