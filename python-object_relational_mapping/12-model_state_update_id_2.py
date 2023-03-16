#!/usr/bin/python3
"""Update the name of a State object from the database hbtn_0e_6_usa.
Usage: ./12-model_state_update_id_2.py
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

    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()
