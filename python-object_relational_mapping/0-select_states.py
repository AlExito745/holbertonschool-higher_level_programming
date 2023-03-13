#!/usr/bin/python3
# List all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \ <mysql password> \ <database name>
    

import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user="mysql username", passwd="mysql password", db="databasena")
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    result = c.fetchall()
    for data in result:
        print(data)
    c.close()
    db.close()
