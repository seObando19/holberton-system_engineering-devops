#!/usr/bin/python3
"""
Python script that, using this REST API(https://jsonplaceholder.typicode.com/),
for a given employee ID, returns information about his/her TODO list progress.

Requirements:

- You must use urllib or requests module
- The script must accept an integer as a parameter, which is the employee ID
- The script must display on the standard output the employee TODO list
    progress
    in this exact format:
        1-First line: Employee EMPLOYEE_NAME is done with
        tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
            * EMPLOYEE_NAME: name of the employee
            * NUMBER_OF_DONE_TASKS: number of completed tasks
            * TOTAL_NUMBER_OF_TASKS: total number of tasks, which is
                the sum of completed and non-completed tasks
        2- Second and N next lines display the title of completed tasks:
        TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
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

    print("Employee {} is done with tasks({}/{})"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for task in completed_task:
        print("\t {}".format(task['title']))
