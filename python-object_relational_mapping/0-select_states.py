#!/usr/bin/python3
#!/usr/bin/python3
# List all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \ <mysql password> \ <database name>


import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user="mysql username", passwd="mysql password", db="database name")
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    dt = c.fetchall()
    for row in dt:
        print(row)
