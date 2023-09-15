#!/usr/bin/python3
"""Lists all State objects containing 'a'"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    my_uname = sys.argv[1]
    my_pwd = sys.argv[2]
    my_db = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(my_uname, my_pwd, my_db))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    has_astates = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id).all()

    for state in has_astates:
        print("{}: {}".format(state.id, state.name))

    session.close()
