#!/usr/bin/python3
"""Prints State objects with name passed as argument"""

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

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    print("{}".format(new_state.id))

    session.close()
