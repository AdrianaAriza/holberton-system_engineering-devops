#!/usr/bin/python3
import csv
import json

import requests
import sys

if __name__ == "__main__":
    cont = 1
    j_dic = {}
    url1 = "https://jsonplaceholder.typicode.com/users/"
    url = "https://jsonplaceholder.typicode.com/todos?userId="
    name = requests.get("{}{}".format(url1, cont)).json()
    f_name = "todo_all_employees.json"
    while name:
        reqs = requests.get("{}{}".format(url, cont)).json()
        rows = []
        for task in reqs:
            t_dict = {}
            t_dict["task"] = task.get("title")
            t_dict["completed"] = task.get("completed")
            t_dict["username"] = name.get("username")
            rows.append(t_dict)
        j_dic[cont] = rows
        cont += 1
        name = requests.get("{}{}".format(url1, cont)).json()
    with open(f_name, 'w') as file:
        file.write(json.dumps(j_dic))
