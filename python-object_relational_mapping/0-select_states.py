#!/usr/bin/python3
# 0-select_states.py
# Alex Nuñez <5694@holbertonstudents.com>
"""List all states from the database hbtn_0e_0_usa.
Arguments:
username: the name user
password: the password of the user
database name: the name database
"""


import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect("username", "password", "databasename")
    c = db.cursor()
    c.execute("SELECT `states` FROM `hbtn_0e_0_usa`
              ORDER BY `s.id`")
    print("({}, {})".format(`s.id`, `states`))
