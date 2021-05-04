#!/usr/bin/python3
"""module
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todo = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()

    user_id = {}
    user_dict = {}
    for users in user:
        userId = users.get('id')
        user_id[userId] = []
        user_dict[userId] = users.get('username')

    for task in todo:
        task_todo = {}
        userId = task.get('userId')
        task_todo['task'] = task.get('title')
        task_todo['completed'] = task.get('completed')
        task_todo['username'] = user_dict.get(userId)
        user_id.get(userId).append(task_todo)

    with open('todo_all_employees.json', 'w') as file:
        json.dump(user_id, file)
