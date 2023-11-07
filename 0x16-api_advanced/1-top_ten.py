#!/usr/bin/python3
"""Module to query the Reddit API and returns the number of subscribers"""
import requests


def top_ten(subreddit: str) -> None:
    """
    Retrieves the top ten posts from a specified subreddit on Reddit and prints
    their titles.

    Args:
        subreddit (str): The name of the subreddit to retrieve the top posts.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        posts = response.json().get("data", {}).get("children", [])
        for post in posts[:10]:
            print(post.get("data", {}).get("title"))
    else:
        print(None)
