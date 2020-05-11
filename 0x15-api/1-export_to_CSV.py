#!/usr/bin/python3
import csv

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    usr = reqs = requests.get(url + "/{}".format(sys.argv[1])).json()
    name = usr.get('username')
    reqs = requests.get('{}/{}/todos'.format(url, sys.argv[1])).json()
    rows = []
    for req in reqs:
        row = []
        row.append(req['userId'])
        row.append(name)
        row.append(req['completed'])
        row.append(req['title'])
        rows.append(row)
    with open("{}.csv".format(row[0]), "w", newline="") as file:
        write = csv.writer(file, delimiter=',',
                           quotechar='"', quoting=csv.QUOTE_ALL)
        write.writerows(rows)
