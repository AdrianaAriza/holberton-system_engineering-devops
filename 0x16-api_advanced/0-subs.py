#!/usr/bin/python3
""""""

import requests


def number_of_subscribers(subreddit):
    """"""
    user_agent = {'User-agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r'
    reqs = requests.get('{}/{}/about.json'.format(url, subreddit),
                        headers={'User-Agent': 'Mozilla/5.0'})
    if reqs.status_code != 200:
        return 0
    return reqs.json()["data"]['subscribers']
