#!/usr/bin/python3
"""a function that queries the Reddit API """
import requests


def number_of_subscribers(subreddit):
    """ Function that queries the Reddit API """
    user_agent = {'User-agent': 'comels'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    req = requests.get(url, headers=user_agent, allow_redirects=False)
    if req.status_code != 404:
        return req.json()['data']['subscribers']
    return 0
