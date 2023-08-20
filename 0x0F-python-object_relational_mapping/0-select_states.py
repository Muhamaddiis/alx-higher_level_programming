#!/usr/bin/python3
"""List all states in the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[0], passwd=sys.argv[1], db=sys.argv[2])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
