#!/usr/bin/python3
'''
Sends  post request to a to a url
'''
if __name__ == "__main__":
    import requests as r
    import sys
    email = sys.argv[2]
    url = sys.argv[1]
    rp = r.post(url, data={'email': email})
    print(rp.text)
