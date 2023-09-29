#!/usr/bin/python3
"""A script that takes 2 arguments to find the
   last 10 commits
"""

import sys
import requests


if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    branch = "master"

    headers = {
            'accept': 'application/vnd.github.v3+json',
            'Authorization': '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',
            'X-GitHub-Api-Version': '2022-11-28',
            }
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?sha={branch}"
    response = requests.get(url, headers=headers)

    commits = response.json()
    count = 0
    for commit in commits:
        if count < 10:
            print(f"{commit['sha']}: {commit['commit']['author']['name']}")
            count += 1
