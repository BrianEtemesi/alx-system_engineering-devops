#!/usr/bin/python3
"""
Given an employee ID, returns TODO info from a REST API and
savess the data to a json file
"""

import csv
import json
import requests
from sys import argv

if __name__ == "__main__":

    # get user object to obtain user attributes
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    res = requests.get(url)
    name = res.json().get('username')

    # get todo list object associated with user
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1])
    res = requests.get(url)
    to_json = res.json()

    # create a dictionary with user todo data
    _dict = {argv[1]: []}

    for tasks in to_json:
        new_dict = {}
        new_dict['task'] = tasks.get('title')
        new_dict['completed'] = tasks.get('completed')
        new_dict['username'] = name
        _dict['{}'.format(argv[1])].append(new_dict)

    # convert dictionary to json format and save to json file
    with open('{}.json'.format(argv[1]), 'w') as file:
        json.dump(_dict, file)
