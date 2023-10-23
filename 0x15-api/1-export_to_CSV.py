#!/usr/bin/python3
"""A Python script that, using this REST API, for a given employee ID."""
import csv
import requests
from sys import argv


def display_tasks():
    """Python script that fetches data for a given employee ID."""
    # link to fetch data from the API
    link = "https://jsonplaceholder.typicode.com/users/"

    # get the data from
    response = requests.get(link + argv[1])

    # convert the data to json format
    data = response.json()

    # get the name of the employee
    name = data.get("name")
    print("Employee {} is done with tasks".format(name), end="")

    # get the total number of tasks of the employee
    response = requests.get(link + argv[1] + "/todos")

    # convert the data to json format
    data = response.json()

    # export as csv file named USER_ID.csv (ex: 2.csv)
    # with columns: "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS","TASK_TITLE"
    with open("{}.csv".format(argv[1]), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in data:
            writer.writerow([argv[1], name, task.get("completed"),
                            task.get("title")])


if __name__ == "__main__":
    display_tasks()
