#!/usr/bin/python3
# Alex Nuñez <5694@holbertonstudents.com>
# 0-select_states.py
# List all states from the database hbtn_0e_0_usa.
# Arguments:
# <mysqlusername>
# <mysql password>
# <mysql database name>
    

import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user="mysql username", passwd="mysql password", db="database name")
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    dt = c.fetchall()
    for row in dt:
        print(row)
