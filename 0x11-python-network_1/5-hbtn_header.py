#!/usr/bin/python3
"""A script that takes URL, sends a request and display
   the 'X-Request-Id'
"""

import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    x_request_var = response.headers["X-Request-Id"]
    print(x_request_var)
