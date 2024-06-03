#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress and exports
the data in JSON format.
"""

from requests import get
from sys import argv
import json

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    todos = response.json()

    response2 = get('https://jsonplaceholder.typicode.com/users')
    users = response2.json()

    for user in users:
        if user.get('id') == int(argv[1]):
            username = user.get('username')
            break

    tasks = []
    for task in todos:
        if task.get('userId') == int(argv[1]):
            task_dict = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            }
            tasks.append(task_dict)

    user_tasks = {str(argv[1]): tasks}

    file_name = '{}.json'.format(argv[1])
    with open(file_name, 'w') as file:
        json.dump(user_tasks, file)

    completed_tasks = [task['task'] for task in tasks if task['completed']]
    print("Employee {} is done with tasks({}/{}):".format(
        username, len(completed_tasks), len(tasks)))
    for task in completed_tasks:
        print("\t {}".format(task))

