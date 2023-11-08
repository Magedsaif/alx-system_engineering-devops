#!/usr/bin/python3
"""Module to query Reddit API and return a list containing the titles of all"""
import requests


def recurse(subreddit, hot_list=[]):
    """Returns a list containing the titles of all hot articles for a given"""
    """subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        for i in range(10):
            title = response.json()["data"]["children"][i]["data"]["title"]
            hot_list.append(title)
        return hot_list
    else:
        return None
