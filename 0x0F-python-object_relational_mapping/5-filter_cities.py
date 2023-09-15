#!/usr/bin/python3
"""Lists all states in a database"""

import MySQLdb
import sys


def dbReader():
    """Lists all the cities of a state in the database. State is
       passed as argument to the script
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysqldb_name = sys.argv[3]
    matched_state = sys.argv[4]

    db = MySQLdb.connect(
            host='localhost', port=3306,
            user=mysql_username, passwd=mysql_password,
            db=mysqldb_name)

    cur = db.cursor()
    queries = "SELECT cities.name FROM cities " \
        "INNER JOIN states ON cities.state_id = states.id " \
        "WHERE states.name = %s " \
        "ORDER BY cities.id ASC"

    cur.execute(queries, (matched_state,))
    matched_cities = cur.fetchall()
    cities_list = [city[0] for city in matched_cities]
    print(', '.join(cities_list))

    cur.close()
    db.close()


if __name__ == '__main__':
    dbReader()
