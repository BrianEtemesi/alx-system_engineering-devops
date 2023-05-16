#!/usr/bin/python3
"""
Contains a recursive function that queries the Reddit API for data
"""
import requests
from collections import Counter


def count_words(subreddit, word_list, after=None):
    """
    Queries the reddit API recursively and prints out a sorted
    count of given keywords
    """

    url = "https://www.reddit.com/r/{}/hot.json?limit=50&after={}".format(
          subreddit, after)
    headers = {'User-Agent': 'Mozilla/5.0'}  # Include a User-Agent header
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        titles = [post['data']['title'] for post in posts]
        words = ' '.join(titles).lower().split()

        word_counts = Counter(words)
        filtered_counts = {word: count
                           for word, count in word_counts.items()
                           if word.lower() in word_list}

        sorted_counts = sorted(filtered_counts.items(),
                               key=lambda x: (-x[1],
                               x[0]))

        for word, count in sorted_counts:
            print("{}: {}".format(word.lower(), count))

        after = data['data']['after']  # Get the 'after' value for pagination

        if after:
            count_words(subreddit, word_list, after)  # Recursive call

    elif response.status_code == 404:
        return None
