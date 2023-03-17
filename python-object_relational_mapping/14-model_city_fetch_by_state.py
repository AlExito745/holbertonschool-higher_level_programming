#!/usr/bin/python3
"""Prints all cities object from the database hbtn_0e_14_usa.
Usage: ./14-model_city_fetch_by_state.py
Arguments:
<mysql username>
<mysql password>
<database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    db = "mysql+mysqldb://{}:{}".format(sys.argv[1], sys.argv[2])
    db += "@localhost/{}".format(sys.argv[3])
    engine = create_engine(db, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id)
    for city, state in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
