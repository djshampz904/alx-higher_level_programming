#!/home/shvmpz/PycharmProjects/alx-higher_level_programming/0x0F-python-object_relational_mapping/myvenv/bin/python3.11
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    state_name = sys.argv[4]

    cur.execute("""SELECT c.name FROM cities AS c INNER JOIN states as s on c.state_id = s.id
                WHERE s.name = %s order by c.id""", (state_name,))

    rows = cur.fetchall()

    # Remove duplicates while preserving order
    unique_rows = list(dict.fromkeys(row[0] for row in rows))

    print(", ".join(unique_rows))

