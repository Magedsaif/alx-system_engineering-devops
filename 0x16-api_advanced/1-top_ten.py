#!/usr/bin/python3
"""Module to query the Reddit API and returns the number of subscribers"""
import requests


def top_ten(subreddit):
    """Returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        for i in range(10):
            title = response.json()["data"]["children"][i]["data"]["title"]
            print(title)
    else:
        print(None)
