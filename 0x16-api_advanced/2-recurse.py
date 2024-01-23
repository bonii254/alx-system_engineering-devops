#!/usr/bin/python3
"""function that queries the Reddit API and returns a list containing the
titles of all hot articles"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """ function that queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyUserAgent"}
    params = {"after": after, "limit": 10}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return None
    results = response.json()["data"]
    hot_list += [post["data"]["title"] for post in results["children"]]
    after = results["after"]
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
