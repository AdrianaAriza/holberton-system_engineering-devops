#!/usr/bin/python3
"""subscribers"""
import requests


def top_ten(subreddit):
    """numbers"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    req = requests.get(url, headers={'User-agent': 'Mozilla/5.0'},
                       params={'limit': '10'})
    if req.status_code != 200:
        print(None)
    req = req.json()
    for r in req['data']['children']:
        print(r['data']['title'])
