#!/usr/bin/python3
"""Uses urllib module for its operations"""

import urllib.request


if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        code = response.read()
        print(code)
