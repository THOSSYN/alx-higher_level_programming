#!/usr/bin/python3
"""Uses urllib module for its operations"""

import urllib.request


if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        code = response.read()
        str_code = code.decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(code)))
        print("\t- content: {}".format(code))
        print("\t- utf8 content: {}".format(str_code))
