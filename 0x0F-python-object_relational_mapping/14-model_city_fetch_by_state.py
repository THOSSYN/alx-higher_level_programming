#!/usr/bin/python3
"""Prints City objects with associated State names from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    my_uname = sys.argv[1]
    my_pwd = sys.argv[2]
    my_db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(my_uname, my_pwd, my_db))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects and access their associated State attributes
    city_list = session.query(City).order_by(City.id).all()

    for city in city_list:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
