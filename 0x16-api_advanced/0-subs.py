# !/usr/bin/python3
"""subscribers"""
import requests


def number_of_subscribers(subreddit):
    """numbers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url, headers={'User-Agent': 'myredditapp:v1.2.3'},
                       allow_redirects=False)
    if req.status_code != 200:
        return 0
    req = req.json()
    return req["data"]["subscribers"]
