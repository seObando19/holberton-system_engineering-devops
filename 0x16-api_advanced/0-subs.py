#!/usr/bin/python3
"""function that queries the Reddit API and returns the number
    of subscribers (not active users, total subscribers) for a
    given subreddit. If an invalid subreddit is given, the function
    should return 0
"""

import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns
    the number of subscribers for a given subreddit"""

    URL = 'https://www.reddit.com/'
    path = 'r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'API advance Sebas'}

    res = requests.get("{}{}".format(URL, path), headers=header)

    if res.status_code == 200:
        return res.json()['data']['subscribers']
    else:
        return 0
