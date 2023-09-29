#!/usr/bin/python3
"""A script that sends a post to an email"""

import sys
import urllib.request
import urllib.parse


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}

    email_data = urllib.parse.urlencode(data).encode('ascii')

    req = urllib.request.Request(url, email_data)

    with urllib.request.urlopen(req) as response:
        response_data = response.read().decode('utf-8')
        print(response_data)
