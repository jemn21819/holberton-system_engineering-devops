#!/usr/bin/python3
"""
Module that use a REST API, for a given employee ID, returns information about
his/her TODO list progress
"""
import requests
import csv
from sys import argv

if __name__ == '__main__':
    employee_id = int(argv[1])
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(employee_id)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(employee_id)).json()

    with open('{}.csv'.format(employee_id), "w") as csv_f:
        data = csv.writer(csv_f, quoting=csv.QUOTE_ALL)
        for task in todo:
            data.writerow(
                [employee_id,
                 user.get('username'),
                 task.get('completed'),
                 task.get('title')])
