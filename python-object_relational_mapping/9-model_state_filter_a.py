#!/usr/bin/python3
"""Lists all State object that contain the letter <a>
from the database hbtn_0e_6_usa.
Usage: ./9-model_state_filter_a.py
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

    result = session.query(State).filter(
        State.name.like("%a%")).order_by(State.id).all()
    for states in result:
        print("{}: {}".format(states.id, states.name))
