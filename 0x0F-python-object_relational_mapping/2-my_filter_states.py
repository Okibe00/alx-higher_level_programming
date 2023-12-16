#!/usr/bin/python3
'''
Module list states matching passed arguments
'''
if __name__ == '__main__':
    import MySQLdb
    import sys
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        port=3306,
        passwd=sys.argv[2],
        charset='utf8',
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states\
            WHERE name = "{}"\
            ORDER BY id ASC'.format(sys.argv[4]))
    query = cursor.fetchall()
    for row in query:
        print(row)
    cursor.close()
    db.close()
