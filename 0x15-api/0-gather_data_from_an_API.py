#!/usr/bin/python3
"""
Python script that, using this REST API(https://jsonplaceholder.typicode.com/),
for a given employee ID, returns information about his/her TODO list progress.
"""


from sys import argv
from requests import get

if __name__ == "__main__":

    employee_id = argv[1]
    URL = "https://jsonplaceholder.typicode.com/"
    user = get('{}users/{}'.format(URL, employee_id)).json()
    EMPLOYEE_NAME = user['name']
    todo = get('{}todos?userId={}'.format(URL, employee_id)).json()
    TOTAL_NUMBER_OF_TASKS = len(todo)
    completed_task = get('{}todos?userId={}&&completed=true'
                         .format(URL, employee_id)).json()
    NUMBER_OF_DONE_TASKS = len(completed_task)
    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for task in completed_task:
        print("\t {}".format(task['title']))
