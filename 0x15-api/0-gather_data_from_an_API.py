#!/usr/bin/python3
"""Python script that, using this REST API
    (https://jsonplaceholder.typicode.com/),
    for a given employee ID, returns information
    about his/her TODO list progress.
"""


from requests import get
from sys import argv

if __name__ == "__main__":

    employee_id = argv[1]
    URL = "https://jsonplaceholder.typicode.com/"

    user = get('{}users/{}'.format(URL, employee_id)).json()
    employee_name = user['name']

    todo = get('{}todos?userId={}'.format(URL, employee_id)).json()
    total_tasks = len(todo)

    completed_task = get('{}todos?userId={}&&completed=true'
                         .format(URL, employee_id)).json()
    done_tasks = len(completed_task)

    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, done_tasks, total_tasks))

    for task in completed_task:
        print("\t {}".format(task['title']))
