#!/usr/bin/python3
"""Define a State model.
Inherits from SQLAlchemy Base and links to the MySQL table states.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represent a state for a MySQL database.

    __tablename__(str): The name of the table to store in States.
    id(sqlalchemy.Integer): The state's id.
    name(sqlalchemy.String): The state's name.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
