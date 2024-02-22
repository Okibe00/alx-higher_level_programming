#!/usr/bin/python3
'''
Sends a request to a server and handle error if any
'''
if __name__ == '__main__':
    from urllib import request, error
    from urllib.error import URLError, HTTPError
    import sys
    url = sys.argv[1]
    try:
        with request.urlopen(url) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
