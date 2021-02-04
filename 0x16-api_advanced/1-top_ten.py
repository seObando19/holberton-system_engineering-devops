#!/usr/bin/python3

"""function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for
    a given subreddit.
"""

import requests


def top_ten(subreddit):
    """function that queries the Reddit
        API and prints the titles of the first 10 hot posts"""
    URL = 'https://www.reddit.com/'
    path = 'r/{}/hot.json?limit=10'.format(subreddit)
    header = {'User-Agent': 'API advance Sebas'}

    res = requests.get("{}{}".format(URL, path), headers=header)

    if res.status_code == 200:
        data = res.json().get('data')
        chidren = data.get('children')

        for child in chidren:
            print(child.get('data').get('title'))
    else:
        print("None")
