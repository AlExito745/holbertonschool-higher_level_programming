#!/usr/bin/python3
"""Displays all values in the states table of the database hbtn_0e_0_usa
whose name matches that supplied as argument.
Usage: ./2-my_filter_states.py
Arguments:
<mysql username>
<mysql password>
<database name>
<state name searched>
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    query = "SELECT * FROM `states`"
    query += "WHERE BINARY `name` = '{}'".format(sys.argv[4])
    c.execute(query)
    result = c.fetchall()
    for data in result:
        print(data)
    c.close()
    db.close()
