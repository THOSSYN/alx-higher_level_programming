#!/usr/bin/python3
"""A script that takes in a url with parameter to send
   a POST request
"""

import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    parameter = {'email': email}
    response = requests.post(url, data=parameter)
    output = response.text
    print(output)
