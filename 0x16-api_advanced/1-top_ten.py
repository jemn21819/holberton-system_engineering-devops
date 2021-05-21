#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """queries the Reddit API"""
    agent = {'User-agent': 'Marisol2201'}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10"
    req = requests.get(url, headers=agent)
    subs = req.json()
    if req.status_code == 404:
        print(None)
    else:
        dict_post = subs["data"]["children"]
        for i in range(len(dict_post)):
            print(dict_post[i]["data"]["title"])
