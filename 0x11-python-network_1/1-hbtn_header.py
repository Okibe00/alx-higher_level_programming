#!/usr/bin/python3
'''
Fetches X-Request-Id header from a response
'''
if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as rs:
        hdr = rs.getheader('X-Request-Id')
        print(hdr)
