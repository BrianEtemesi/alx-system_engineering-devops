#!/usr/bin/python3
"""
Given an employee ID, returns TODO info from a REST API
"""

import json
import requests
from sys import argv

if __name__ == "__main__":

    # get user object to obtain user attributes
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    res = requests.get(url)
    name = res.json().get('name')

    # get todo list object associated with user
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1])
    res = requests.get(url)
    to_json = res.json()

    # calculate number of completed tasks
    done = 0
    for task in to_json:
        if task['completed'] is True:
            done += 1

    # total number of tasks
    total = len(to_json)

    print("Employee {} is done with tasks({}/{}):".format(name, done, total))

    # print title of completed tasks
    for task in to_json:
        if task['completed'] is True:
            print("\t {}".format(task['title']))
