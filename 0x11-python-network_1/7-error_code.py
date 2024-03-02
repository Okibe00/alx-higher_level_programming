#!/usr/bin/python3
'''
prints error code the error code
'''
if __name__ == '__main__':
    import sys
    import requests as r

    url = sys.argv[1]
    resp = r.get(url)
    if resp.status_code >= 400:
        print("Error code: {}".format(resp.status_code))
    else:
        print(resp.text)
