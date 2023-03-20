#!/usr/bin/python3
"""Script that lists all cities\
        from the database hbtn_0e_4_usa"""

import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print("Usage: {} username\
                password database".format(args[0]))
        exit(1)

    username = args[1]
    password = args[2]
    database = args[3]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8")
        cursor = db.cursor()
        query = "SELECT * FROM cities\
                ORDER BY id ASC"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error [{}]:\
                {}".format(e.args[0], e.args[1]))
        exit(1)
