#!/usr/bin/python3
"""Creates a state with a city from a database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch State objects and their associated City objects, sorting both by ID
    state_list = session.query(State).order_by(State.id).all()

    for state in state_list:
        print("{}: {}".format(state.id, state.name))
        # Sort the associated City objects by ID
        for city in sorted(state.cities, key=lambda c: c.id):
            print("    {}: {}".format(city.id, city.name))

    session.close()
