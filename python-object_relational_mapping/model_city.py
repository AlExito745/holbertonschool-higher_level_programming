#!/usr/bin/python3
"""Define a City model.
Inherits from SQLAlchemy Base and links to the MySQL table states.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

Base = declarative_base()


class City(Base):
    """Represent a city for a MySQL database.
    
    __tablename__(str): The name of the table to store in Cities.
    id(sqlalchemy.Integer): The state's id.
    name(sqlalchemy.String): The state's name.
    state_id(sqlalchemy.Integer): The city's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state_id'), nullable=False)
