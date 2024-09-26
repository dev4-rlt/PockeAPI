from core.database import db
from sqlalchemy import Column, Integer, String

class Users(db.Model):
    __tablename__ = "users"

    codUser = Column(name='cod_user', type_=Integer, primary_key=True, autoincrement=True)
    name = Column(name='name', type_=String, nullable=False)
    username = Column(name='username', type_=String, nullable=False)
    password = Column(name='password', type_=String, nullable=False)
    address = Column(name='address', type_=String)