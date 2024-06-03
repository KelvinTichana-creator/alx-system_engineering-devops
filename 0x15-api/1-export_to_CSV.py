#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress and exports
the data in CSV format.
"""

from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    # Fetch the TODO list data
    response = get('https://jsonplaceholder.typicode.com/todos/')
    todos = response.json()
    
    # Fetch the user data
    response2 = get('https://jsonplaceholder.typicode.com/users')
    users = response2.json()

    # Get the employee name and username
    for user in users:
        if user.get('id') == int(argv[1]):
            employee_name = user.get('name')
            username = user.get('username')

    # Prepare the data for CSV
    tasks = []
    for task in todos:
        if task.get('userId') == int(argv[1]):
            tasks.append([
                task.get('userId'),
                username,
                task.get('completed'),
                task.get('title')
            ])

    # Define the CSV file name
    file_name = '{}.csv'.format(argv[1])

    # Write to CSV file
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow(task)

    # Print the result to the standard output
    completed_tasks = [task[3] for task in tasks if task[2]]
    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(completed_tasks), len(tasks)))
    for task in completed_tasks:
        print("\t {}".format(task))

