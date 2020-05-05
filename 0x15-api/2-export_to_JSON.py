#!/usr/bin/python3
import csv
import json

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    usr = reqs = requests.get(url + "/{}".format(sys.argv[1])).json()
    name = usr.get('username')
    reqs = requests.get('{}/{}/todos'.format(url, sys.argv[1])).json()
    rows = []
    j_dict = {}
    for req in reqs:
        dict = {}
        dict["task"] = req.get("title")
        dict["completed"] = req.get("completed")
        dict["username"] = name
        rows.append(dict)
    j_dict[req.get('userId')] = rows
    with open('{}.json'.format(req.get('userId')), 'w') as file:
        json.dump(j_dict, file)
