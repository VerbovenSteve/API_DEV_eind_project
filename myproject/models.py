from fastapi.dependencies import models
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, Session
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)



class Film(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    release_year = Column(Integer, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    characters = relationship('Person', back_populates='film')
    starships = relationship('Starship', back_populates='film')



class Person(Base):
    __tablename__ = 'personages'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False, index=True)
    age = Column(Integer, index=True)
    film_id = Column(Integer, ForeignKey('films.id'))

    film = relationship('Film', back_populates='characters')

class Starship(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False)
    model = Column(String, index=True)
    film_id = Column(Integer, ForeignKey('films.id'))

    film = relationship('Film', back_populates='starships')