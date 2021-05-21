#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """recursive function that queries the Reddit API"""
    headers = {'User-agent': 'James1986'}
    base = 'https://www.reddit.com/'
    query = '/r/{}/hot.json?after={}'.format(subreddit, after)
    response = requests.get(base + query, headers=headers)
    top = response.json().get('data', {}).get('children', [])
    after = response.json().get('data', {}).get('after', None)
    if not top:
        return None
    for post in top:
        hot_list.append(post.get('data').get('title'))
    if not after:
        return hot_list
    return recurse(subreddit, hot_list, after)
