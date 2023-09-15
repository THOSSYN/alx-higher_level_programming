#!/usr/bin/python3
"""Lists all states in a database"""

import MySQLdb
import sys


def dbReader():
    """Lists all the states in the database
       passed as argument to it that starts with uppercase 'N'
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysqldb_name = sys.argv[3]
    matched_name = sys.argv[4]

    db = MySQLdb.connect(
            host='localhost', port=3306,
            user=mysql_username, passwd=mysql_password,
            db=mysqldb_name)
    cur = db.cursor()

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY\
            id ASC".format(matched_name)

    cur.execute(query)
    matched = cur.fetchall()
    for state in matched:
        print(state)

    cur.close()
    db.close()


if __name__ == '__main__':
    dbReader()
