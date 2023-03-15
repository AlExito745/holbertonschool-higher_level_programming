#!/usr/bin/python3
"""Take a name of state as argument that
lists all cities of that state using the database hbtn_0e_4_usa.
Usage: ./5-filter_cities.py
Arguments:
<mysql username>
<mysql password>
<database name>
<state name>
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    query = "SELECT * FROM `cities` AS `c` INNER JOIN \
        `states` AS `s`"
    query += "ON `c`.`state_id` = `s`.`id` ORDER BY `c`.`id` ASC"
    c.execute(query)
    result = c.fetchall()
    print(", ".join([data[2] for data in result if sys.argv[4] == data[4]]))
    c.close()
    db.close()
