#!/usr/bin/python3
"""a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ Function recurse """
    user_agent = {'User-agent': 'comels'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    req = requests.get(url,
                       headers=user_agent,
                       allow_redirects=False,
                       params={'after': after})
    if req.status_code == 404:
        return None

    hot = req.json()['data']
    after = hot['after']

    for result in hot['children']:
        hot_list.append(result['data']['title'])

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
