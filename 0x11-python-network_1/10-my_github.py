#!/usr/bin/python3
"""A script that takes GitHub credential and display your
   account information
"""

import sys
import requests


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]

    session = requests.Session()
    session.auth = (username, password)

    headers = {
            'Accept': 'application/vnd.github.v3+json',
            'X-GitHub-Api-Version': '2022-11-28'
            }

    url = "https://api.github.com/THOSSYN"

    response = session.get(url, headers=headers)
    dict_json = response.json()
    ID = dict_json.get('id')
    print(ID)
