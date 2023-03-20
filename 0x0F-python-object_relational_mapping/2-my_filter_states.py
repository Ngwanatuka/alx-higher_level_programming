#!/usr/bin/python3
"""
This module runs a script that searches the states table
for a given state name.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    get the command line arguments
    """
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    """
    connect to the database
    """
    db = MySQLdb.connect(
        host='localhost',
        user=mysql_user,
        passwd=mysql_password,
        db=db_name,
        port=3306
    )

    """
    get a cursor object
    """
    cursor = db.cursor()

    """
    execute the query
    """
    query = "SELECT * FROM states WHERE\
            name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    """
    get result
    """
    result = cursor.fetchall()

    """
    print the results
    """
    for row in result:
        print(row)

    """
    close the database connection
    """
    db.close()
