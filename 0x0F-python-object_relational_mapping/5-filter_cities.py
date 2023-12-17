#!/usr/bin/python3
'''
Module: gets city from user input
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
    val = sys.argv[4]
    query = 'SELECT c.name FROM cities c\
            JOIN states s ON c.state_id = s.id\
            WHERE s.name = %s\
            ORDER BY c.id ASC'
    cursor.execute(query, (val,))
    rows = cursor.fetchall()
    city_list = list()
    for row in rows:
        for col in row:
            city_list.append(col)
    for i in range(len(city_list)):
        if (i == len(city_list) - 1):
            print(city_list[i])
        else:
            print(city_list[i] + ', ', end='')
    cursor.close()
    db.close()
