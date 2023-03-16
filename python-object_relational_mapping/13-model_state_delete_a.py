#!/usr/bin/python3
"""Delete all State object that containing the letter <a>
from tha database hbtn_0e_6_usa
Usage: ./13-model_state_delete_a.py
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

    states = session.query(State)
    for state in states:
        if "a" in state.name:
            session.delete(state)
    session.commit()
