#!/usr/bin/python3
""""""

import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if req.status_code != 200:
        return 0
    req = req.json()
    return req["data"]["subscribers"]
