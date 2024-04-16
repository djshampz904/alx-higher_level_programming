#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    passwd="toor",
    user="shvmpz",
    db="hbtn_0e_0_usa"
)

cur = db.cursor()

cur.execute("SELECT * FROM states ORDER BY id ASC")

for row in cur.fetchall():
    print(row)

db.close()