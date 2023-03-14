#!/usr/bin/python3
"""List all states with a name starting with N.
Usage: ./1-filter_states.py
<mysql username>
<mysql password>
<database name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    query = "SELECT * FROM `states` WHERE `name` LIKE 'N%'"
    c.execute(query)
    result = c.fetchall()
    for data in result:
        print(data)
    c.close()
    db.close()
