#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv

if __name__ == "__main__":
    # Fetch the TODO list data
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()    
    # Fetch the user data
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()
    # Initialize variables
    completed = 0
    total = 0
    tasks = []
    # Get the employee name
    for i in data2:
        if i.get('id') == int(argv[1]):
            employee = i.get('name')
    # Count the tasks and gather titles of completed tasks
    for i in data:
        if i.get('userId') == int(argv[1]):
            total += 1
            if i.get('completed'):
                completed += 1
                tasks.append(i.get('title'))
    # Print the result
    print("Employee {} is done with tasks({}/{}):".format(employee, completed,
                                                          total))
    for task in tasks:
        print("\t {}".format(task))
