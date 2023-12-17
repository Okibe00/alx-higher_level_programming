#!/usr/bin/python3
'''
Module constructs a query from user input
'''

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
        charset='utf8'
    )
    cursor = db.cursor()
    val = sys.argv[4]
    query = 'SELECT * FROM states\
            WHERE name=%s'
    cursor.execute(query, (val,))
    for row in cursor:
        print(row)
    cursor.close()
    db.close()
