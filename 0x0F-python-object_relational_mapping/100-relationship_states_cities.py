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

    create_state = State(name='California')
    create_city = City(name='San Francisco', state=create_state)
    session.add(create_state)
    session.add(create_city)
    session.commit()

    session.close()
