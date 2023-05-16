#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts listed
for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    retrieves data for a given subreddit using a get request
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}  # include a User_Agent header
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children'][:10]  # retrieve the first 10 posts
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print(None)


if __name__ == "__main__":

    topics = top_ten('Formula1')
