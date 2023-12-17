#!/usr/bin/python3
'''
Module list all cities in the database
'''
if __name__ == '__main__':
    import MySQLdb
    import sys
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset='utf8'
    )
    cursor = db.cursor()
    query = 'SELECT c.id, c.name, s.name FROM cities c\
            JOIN states s ON c.state_id = s.id\
            ORDER BY c.id ASC'
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
