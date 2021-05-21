#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """"queries the Reddit API"""
    agent = {'User-agent': 'James1986'}
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    req = requests.get(url, headers=agent)
    subs = req.json()
    if req.status_code == 404:
        return (0)
    else:
        return(subs["data"]["subscribers"])
