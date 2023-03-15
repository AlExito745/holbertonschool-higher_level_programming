#!/usr/bin/python3
"""List all cities from the database hbtn_0e_4_usa.
Usage: ./4-cities_by_state.py
Arguments:
<mysql username>
<mysql password>
<database name>
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    query = "SELECT `c`.`id`, `c`.`name`, `s`.`name` FROM `cities` AS `c` \
        INNER JOIN `states` AS `s`"
    query += "ON `c`.`state_id` = `s`.`id` ORDER BY `c`.`id` ASC"
    c.execute(query)
    result = c.fetchall()
    for data in result:
        print(data)
    c.close()
    db.close()
