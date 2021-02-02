#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python
    script to export data in the CSV format.
"""

import csv
from requests import get
from sys import argv

if __name__ == "__main__":
    employee_id = argv[1]
    URL = "https://jsonplaceholder.typicode.com/"
    user = get("{}users/{}".format(URL, employee_id)).json()
    todo = get('{}todos?userId={}'.format(URL, employee_id)).json()

    # Export data to CSV
    fileCreate = "{}.csv".format(employee_id)
    with open(fileCreate, "w") as csv_file:
        f = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for row in todo:
            f.writerow([user['id'],
                        user['username'],
                        row['completed'],
                        row['title']])
