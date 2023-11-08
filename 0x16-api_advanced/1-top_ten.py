#!/usr/bin/python3
"""sumary_line
"""
import requests


def top_ten(subreddit):
    """sumary_line
    """
    
    url = "https://api.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Custom)'}
    response = requests.get(url, headers=headers, params={"limit": 10})

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print(None)
