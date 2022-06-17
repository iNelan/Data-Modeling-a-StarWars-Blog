import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class  Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}


    # AQUI EMPIEZAAAAAAAAAAAAAAAAAAAAAAAAAAA

class  User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    addresses = relationship('Favourites', backref='user', lazy=True)


class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    addresses = relationship('Favourites', backref='characters', lazy=True)


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    diameter = relationship('Favourites', backref='planets', lazy=True)


class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lenght = Column(String(250), nullable=False)
    passengers = Column(String(250), nullable=False)
    cost = relationship('Favourites', backref='vehicles', lazy=True)


class Favourites(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)
    
    user_id = Column(Integer, ForeignKey('user.id'),
        nullable=False)
    characters_id = Column(Integer, ForeignKey('characters.id'),
        nullable=False)
    planets_id = Column(Integer, ForeignKey('planets.id'),
        nullable=False)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'),
        nullable=False)






    def to_dict(self):
        return {}
        
        







## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')