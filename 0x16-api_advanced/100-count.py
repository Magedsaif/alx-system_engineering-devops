#!/usr/bin/python3
"""Module to query the Reddit API and returns the number of subscribers"""
import requests


def count_words(subreddit, word_list, after=None, word_dict={}):
    """Returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        for i in range(100):
            title = response.json()["data"]["children"][i]["data"]["title"]
            for word in word_list:
                if word.lower() in title.lower():
                    if word in word_dict:
                        word_dict[word] += 1
                    else:
                        word_dict[word] = 1
        after = response.json()["data"]["after"]
        if after is None:
            for key, value in sorted(word_dict.items(),
                                     key=lambda x: (-x[1], x[0])):
                if value != 0:
                    print("{}: {}".format(key, value))
            return
        return count_words(subreddit, word_list, after, word_dict)
    else:
        return
