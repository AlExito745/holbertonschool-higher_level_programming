#!/usr/bin/python3
"""Adds a new State object to database hbtn_0e_6_usa.
Usage: ./11-model_state_insert.py
Arguments:
<mysql username>
<mysql password>
<database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    db = "mysql+mysqldb://{}:{}".format(sys.argv[1], sys.argv[2])
    db += "@localhost/{}".format(sys.argv[3])
    engine = create_engine(db, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print("{}".format(new_state.id))
