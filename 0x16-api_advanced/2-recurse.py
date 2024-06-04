#!/usr/bin/python3
"""a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ Function recurse """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'custom'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        r = r.json()
        for post in r.get('data').get('children'):
            hot_list.append(post.get('data').get('title'))
        if r.get('data').get('after'):
            recurse(subreddit, hot_list)
        return hot_list
    else:
        return None
