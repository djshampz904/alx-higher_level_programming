#!/usr/bin/python3
# script should take 4 arguments: mysql username, mysql password, database name and state name searched(safe from MySQL injection)
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        passwd=sys.argv[2],
        user=sys.argv[1],
        db=sys.argv[3],
        port=3306
    )

    searched = sys.argv[4]
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE %s "
                "ORDER BY states.id ASC", (searched,))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()