#!/usr/bin/python3
'''
post an email address
'''

if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    email = sys.argv[2]
    with urllib.request.urlopen(url, email) as rs:
        print(rs.read().decode('utf-8'))
