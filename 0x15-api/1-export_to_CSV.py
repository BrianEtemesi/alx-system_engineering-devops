#!/usr/bin/python3
"""
Given an employee ID, returns TODO info from a REST API and
copies the data to a CSV file
"""

import csv
import json
import requests
from sys import argv

if __name__ == "__main__":

    # get user object to obtain user attributes
    user_id = int(argv[1])
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    res = requests.get(url)
    name = res.json().get('name')

    # get todo list object associated with user
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    res = requests.get(url)
    to_json = res.json()

    # create a CSV file with format USER_ID.csv
    file_name = "{}.csv".format(argv[1])
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        # copy data to CSV file
        for task in to_json:
            writer.writerow([task['userId'], name, task['completed'], task['title']])
