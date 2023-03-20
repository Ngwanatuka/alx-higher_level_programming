#!/usr/bin/python3
"""Script that takes in arguments\
        and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument.
    Safe from MySQL injections!
"""

import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 5:
        print("Usage: {} username password\
                database state_name".format(args[0]))
        exit(1)

    username = args[1]
    password = args[2]
    database = args[3]
    state_name = args[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8")
        cursor = db.cursor()
        query = "SELECT * FROM states\
                WHERE name=%s ORDER BY id ASC"
        cursor.execute(query, (state_name,))
        results = cursor.fetchall()
        for row in results:
            print(row)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error [{}]:\
                {}".format(e.args[0], e.args[1]))
        exit(1)
