#!/usr/bin/python3
'''
post an email address
'''

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    url = sys.argv[1]
    email = sys.argv[2]
    data = {
        'email': email
    }
    data = urllib.parse.urlencode(data)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as rs:
        print(rs.read().decode('utf-8'))
