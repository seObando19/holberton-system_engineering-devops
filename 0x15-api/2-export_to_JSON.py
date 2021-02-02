#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python script
    to export data in the JSON format.
"""


import json
from requests import get
from sys import argv

if __name__ == "__main__":
    employee_id = argv[1]
    URL = "https://jsonplaceholder.typicode.com/"
    user = get("{}users/{}".format(URL, employee_id)).json()
    todo = get('{}todos?userId={}'.format(URL, employee_id)).json()

    # Export data to json
    fileCreate = "{}.json".format(employee_id)
    tasks = []
    for task in todo:
        tasks_dict = {}
        tasks_dict["task"] = task.get('title')
        tasks_dict["completed"] = task.get('completed')
        tasks_dict["username"] = user.get('username')
        tasks.append(tasks_dict)

    obj = {}
    obj[employee_id] = tasks
    with open(fileCreate, "w") as json_file:
        json.dump(obj, json_file)
