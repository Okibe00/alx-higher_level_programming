#!/usr/bin/python3
'''
Module: Fetches a url
'''

if __name__ == '__main__':
    import urllib.request
    url = 'https://alx-intranet.hbtn.io/status'
    try:
        with urllib.request.urlopen(url) as response:
            page = response.read()
            page_type = type(page)
            page_encoding = page.decode('utf-8')
            print("Body response:")
            print('\t- type: {}'.format(page_type))
            print('\t- content: {}'.format(page))
            print('\t- utf8 content: {}'.format(page_encoding))
    except Exception as e:
        print(e)
