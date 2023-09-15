#!/usr/bin/python3
"""Lists all states in a database"""

import MySQLdb
import sys


def main():
    """Lists all the states in the database
       passed as argument to it
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysqldb_name = sys.argv[3]

    db = MySQLdb.connect(
            host='localhost', port=3306,
            user=mysql_username, passwd=mysql_password,
            db=mysqldb_name)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
