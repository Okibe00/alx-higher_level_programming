#!/usr/bin/python3
'''
Fetches header X-Request-Id
'''
if __name__ == '__main__':
    import sys
    import requests
    url = sys.argv[1]
    rq = requests.get(url)
    if rq.headers.get('X-Request-Id', 0):
        print("{}".format(rq.headers['X-Request-Id']))
