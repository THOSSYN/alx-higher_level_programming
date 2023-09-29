#!/usr/bin/python3
"""A script that takes a url and sends request and display
   the body with status ocde
"""

import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= int(400):
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
