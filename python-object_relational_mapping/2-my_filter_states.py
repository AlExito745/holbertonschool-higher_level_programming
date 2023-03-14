#!/usr/bin/python3
"""Take an argument and display all values of a table on database.
Arguments:
<mysql username>
<mysql password>
<database name>
<state name searched>
"""

import sys
import MySQLdb

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
c = db.cursor()
query = "SELECT * FROM `states`"
c.execute(query)
result = c.fetchall()
for data in result:
    if sys.argv[4] == data[1]:
        print(data)
c.close()
db.close()
