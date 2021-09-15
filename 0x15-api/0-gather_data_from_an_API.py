#!/usr/bin/python3
"""
use RESTapi to return information needed.
"""
import requests
from sys import argv

if __name__ == "__main__":
    emp_id = int(argv[1])
    url1 = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)
    r = requests.get(url1).json()
    name = r.get("name")
    done = 0
    total = 0
    all_tasks = []
    url2 = 'https://jsonplaceholder.typicode.com/todos/'
    for i in requests.get(url2).json():
        if i.get('userId') == emp_id:
            total += 1
            if i.get('completed'):
                done += 1
                all_tasks.append(i.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(name, done, total))
    for task in all_tasks:
        print('\t {}'.format(task))
