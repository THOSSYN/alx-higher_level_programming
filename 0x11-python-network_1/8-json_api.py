#!/usr/bin/python3
"""A script that takes a letter, sends a POST request
   to a url with the letter as parameter
"""

import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) < 2:
        arg = ""
    else:
        arg = sys.argv[1]

    param_data = {'q': arg}

    url = "http://0.0.0.0:5000/search_user"

    response = requests.post(url, data=param_data)

    json_dict = response.json()
    try:
        if json_dict:
            print("[{}] {}".format(json_dict.get('id'), json_dict.get('name')))
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
