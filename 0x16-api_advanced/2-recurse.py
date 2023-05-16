#!/usr/bin/python3
"""
Contains a recursive function that queries the reddit API and
returns a list containing the titles of all hot articles for
a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    recursively queries the reddit API to return all hot articles
    for a give subreddit
    """

    url = "https://www.reddit.com/r/{}/hot.json?limit=50&after={}".format(
          subreddit, after)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        after = data['data']['after']

        if after:
            recurse(subreddit, hot_list, after)

    elif response.status_code == 404:
        return None

    return hot_list


if __name__ == '__main__':

    all_topics = recurse('fintech')
    print(len(all_topics))
