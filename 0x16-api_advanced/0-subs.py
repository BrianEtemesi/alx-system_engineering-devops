#!/usr/bin/python3
"""
Returns the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    retrieves number of subscribers for a
    given subreddit from the reddit API
    """

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}  # include a User-Agent header
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0


if __name__ == '__main__':

    fans = number_of_subscribers("quantumcomputing")
    print(fans)
