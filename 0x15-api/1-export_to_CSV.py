#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress."""
import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    completed = [t.get("title") for t in todos if t.get("completed") is True]
    username = user.get("name")

    with open("{}.csv".format(user_id), "w") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for t in todos:
            csv_writer.writerow(
                [user_id, username, t.get("completed"), t.get("title")])
