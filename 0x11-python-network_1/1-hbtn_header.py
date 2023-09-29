#!/usr/bin/python3
"""A script that displays the header value 'X-Request-Id '"""

import sys
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    #head_var = "X-Request-Id"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        x_request_id = response.headers['X-Request-Id']
        print(x_request_id)
