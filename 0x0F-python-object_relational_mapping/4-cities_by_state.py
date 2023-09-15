#!/usr/bin/python3
""" a script that lists all cities from a database"""

import MySQLdb
import sys


def dbReader():
    """ a script that lists all cities from the database
        hbtn_0e_4_usa
    """
    my_uname = sys.argv[1]
    my_pwd = sys.argv[2]
    my_dbname = sys.argv[3]

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=my_uname,
            passwd=my_pwd,
            db=my_dbname)

    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities "\
            "INNER JOIN states ON cities.state_id = states.id "\
            "ORDER BY cities.id ASC"

    cur.execute(query)
    cities_names = cur.fetchall()
    for city in cities_names:
        print(city)

    cur.close()
    db.close()


if __name__ == '__main__':
    dbReader()
