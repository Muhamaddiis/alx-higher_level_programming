#!/usr/bin/python
"""script that lists all states with a name starting upperase N"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[0], passwd=sys.argv[1], db=sys.argv[2])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY `id`")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
