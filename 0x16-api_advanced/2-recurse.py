#!/usr/bin/python3
"""subscribers"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """numbers"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    req = requests.get(url, headers={'User-agent': 'Mozilla/5.0'},
                       params={'after': after}, allow_redirects=False)
    if req.status_code != 200:
        return None
    req = req.json()
    for r in req['data']['children']:
        hot_list.append(r['data']['title'])
    if req['data']['after']:
        recurse(subreddit, hot_list, req['data']['after'])
    return hot_list
