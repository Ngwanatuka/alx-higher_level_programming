#!/usr/bin/python3
"""This module runs a script that selects
states that start with N
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """get the command line arguments
    """
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    """Connect to the database
    """

    db = MySQLdb.connect(
            host='localhost',
            user=mysql_user,
            passwd=mysql_password,
            db=db_name,
            port=3306
            )
    """get a cursor object
    """

    cursor = db.cursor()

    """Execute the query
    """
    cursor.execute("SELECT * FROM states WHERE name\
            LIKE 'N%' ORDER BY states.id")

    """Get the result
    """
    result = cursor.fetchall()
    """Print the results
    """
    for row in result:
        print(row)

    """Close the database connection
    """
    db.close
