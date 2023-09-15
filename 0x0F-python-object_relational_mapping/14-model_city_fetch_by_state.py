#!/usr/bin/python3
"""prints all City objects from database"""

from sqlalchemy import text, create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == '__main__':
    my_uname = sys.argv[1]
    my_pwd = sys.argv[2]
    my_db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(my_uname, my_pwd, my_db))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    statemt = text("SELECT states.name, cities.id, cities.name "
                   "FROM cities "
                   "INNER JOIN states ON cities.state_id = states.id "
                   "ORDER BY cities.id ASC")

    get_query = session.query(City).from_statement(statemt).all()

    for city in get_query:
        print("{}: {} {}".format(city.state.name, city.id, city.name))

    session.close()
