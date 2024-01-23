#!/usr/bin/python3
""" queries the Reddit API and prints the titles of the first 10 hot posts"""

import requests


def top_ten(subreddit):
    """ queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyUserAgent"}
    params = {"limits": 10}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data").get("children")
    [print(val.get("data").get("title")) for val in results]
