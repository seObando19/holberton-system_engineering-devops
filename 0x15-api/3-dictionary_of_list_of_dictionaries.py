#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python script
    to export data in the JSON format.
"""


import json
from requests import get


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    users = get("https://jsonplaceholder.typicode.com/users").json()

    # Export data to json
    userdict = {}
    usernamedict = {}
    for user in users:
        uid = user.get("id")
        userdict[uid] = []
        usernamedict[uid] = user.get("username")
        todo = get("https://jsonplaceholder.typicode.com/todos").json()

    for task in todo:
        taskdict = {}
        uid = task.get("userId")
        taskdict["task"] = task.get('title')
        taskdict["completed"] = task.get('completed')
        taskdict["username"] = usernamedict.get(uid)
        userdict.get(uid).append(taskdict)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(userdict, jsonfile)
