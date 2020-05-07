#!/usr/bin/python3
import sys

import requests

def number_of_subscribers(subreddit):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r'
    reqs = requests.get('{}/{}/about.json'.format(url, sys.argv[1]), headers=user_agent).json()
    print(reqs)
    return reqs["data"]['subscribers']
