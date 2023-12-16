#!/usr/bin/python3
'''
Module list all states in a database
'''
if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=f'{sys.argv[1]}',
        passwd=sys.argv[2],
        db=f'{sys.argv[3]}',
        charset='utf8'
    )
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id ASC')
    query_res = cursor.fetchall()
    for row in query_res:
        print(row)
    cursor.close()
    db.close()
