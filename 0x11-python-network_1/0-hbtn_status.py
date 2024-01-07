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
            print(f'\t - type: {page_type}')
            print(f'\t - content: {page}')
            print(f'\t - utf8 content: {page_encoding}')
    except Exception as e:
        print(e)
