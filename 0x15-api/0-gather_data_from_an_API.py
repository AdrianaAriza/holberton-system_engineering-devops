#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    reqs = requests.get('{}/{}/todos'.format(url, sys.argv[1])).json()
    x = len(reqs)
    d_task = []
    for req in reqs:
        if req['completed'] is True:
            d_task.append('\t {}'.format(req['title']))
    reqs = requests.get(url + "/{}".format(sys.argv[1])).json()
    print('Employee {} is done with tasks({}/{}):'.format(reqs.get('name'),
          len(d_task), x))
    for task in d_task:
        print(task)
