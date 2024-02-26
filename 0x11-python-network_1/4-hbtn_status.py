#!/usr/bin/python3
'''
fetch a url using request module
'''
if __name__ == "__main__":
    import requests
    url = 'https://alx-intranet.hbtn.io/status'
    resp = requests.get(url)
    text = resp.text
    print("Body response:")
    print('\t- type: {}'.format(type(text)))
    print('\t- content: {}'.format(text))
