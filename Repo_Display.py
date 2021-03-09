"""
Author: Yikan Wang
This file contains a program that takes user name of Github
And prints out the number of commits

I pledge my honor that all HW was done by myself
"""

import requests
import json


def get_repo_info(user_name: str):
    result = []
    user_url = 'https://api.github.com/users/{}/repos'.format(user_name)
    res = requests.get(user_url)
    repos = json.loads(res.text)

    try:
        repos[0]['name']
    except (IndexError, TypeError, KeyError):
        return 'Cannot Get Repo From This User'

    try:
        for repo in repos:
            name = repo['name']
            url = 'https://api.github.com/repos/{}/{}/commits'.format(user_name, name)
            info = requests.get(url)
            info_json = json.loads(info.text)
            result.append('Repo: {} Number of commits: {}'.format(name, len(info_json)))
    except (IndexError, TypeError, KeyError):
        return 'Cannot Get Repo From This User'
    # for better testing purposes, I return the 'result'
    # instead of printing it here
    return result


if __name__ == '__main__':
    #calls the method
    res = get_repo_info(user_name='wanismvp')
    for line in res:
        print(line)
