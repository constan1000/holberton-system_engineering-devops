#!/usr/bin/python3
""" Gather data needed for a given employee ID """
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        respond1 = requests.get('https://jsonplaceholder.typicode.com/todos')
        respond2 = requests.get('https://jsonplaceholder.typicode.com/users')
        search1 = respond1.json()
        search2 = respond2.json()
        for i in search2:
            if i['id'] == int(sys.argv[1]):
                us = i['name']
        count = 0
        completed = 0
        tasks = []
        for i in search1:
            for key, value in i.items():
                if key == 'userId' and value == int(sys.argv[1]):
                    count += 1
                    for key, value in i.items():
                        if key == 'completed' and value is True:
                            completed += 1
                            tasks.append(i['title'])
        print('Employee {} is done with tasks\
({}/{}):'.format(us, completed, count))
        for i in tasks:
            print('\t {}'.format(i))