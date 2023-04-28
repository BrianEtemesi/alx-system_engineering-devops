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
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    res = requests.get(url)
    full_name = res.json().get('name')
    names = full_name.split()
    name = names[0]

    # get todo list object associated with user
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1])
    res = requests.get(url)
    to_json = res.json()

    # create a CSV file with format USER_ID.csv
    file_name = "{}.csv".format(argv[1])
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        # copy data to CSV file
        for task in to_json:
            writer.writerow([argv[1], name, task['completed'], task['title']])
