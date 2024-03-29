#!/usr/bin/python3
"""
a script that changes the name of a State object from
the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # makes engine for database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # it finds and updates state (run #7 to see table printed)
    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"

    session.commit()
    session.close()
