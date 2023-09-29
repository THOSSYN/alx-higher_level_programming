#!/usr/bin/python3
"""A script that fetches a url"""

import requests


if __name__ == '__main__':
    response = requests.get('https://alx-intranet.hbtn.io/status')
    body = response.text
    print("Body response:")
    print("    - type: {}".format(type(body)))
    print("    - content: {}".format(body))
