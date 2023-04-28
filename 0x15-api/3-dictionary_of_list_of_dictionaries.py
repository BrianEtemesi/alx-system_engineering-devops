#!/usr/bin/python3
"""
Given an employee ID, returns TODO info from a REST API and
savess the data to a json file
"""

import json
import requests
from sys import argv

if __name__ == "__main__":

    main_dict = {}

    # loop through all 10 users to get their todos

    for i in range(1, 11):
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(i)
        res = requests.get(url)
        name = res.json().get('username')

        url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(i)
        res = requests.get(url)
        to_json = res.json()

        _dict = {str(i): []}

        for tasks in to_json:
            new_dict = {}
            new_dict['username'] = name
            new_dict['task'] = tasks.get('title')
            new_dict['completed'] = tasks.get('completed')
            _dict['{}'.format(str(i))].append(new_dict)

        for item in _dict:
            main_dict[item] = _dict[item]

    # copy dictionary to json file in json format

    with open('todo_all_employees.json', 'w') as file:
        json.dump(main_dict, file)
