#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        passwd=sys.argv[2],
        user=sys.argv[1],
        db=sys.argv[3]
    )

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()