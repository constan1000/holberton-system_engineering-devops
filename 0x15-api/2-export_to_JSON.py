#!/usr/bin/python3
""" Exporting to JSON """
import json
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        respond1 = requests.get('https://jsonplaceholder.typicode.com/todos')
        respond2 = requests.get('https://jsonplaceholder.typicode.com/users')
        search1 = respond1.json()
        search2 = respond2.json()
        for y in search2:
            if y['id'] == int(sys.argv[1]):
                user = y['name']
                usern = y['username']
        Max = 0
        Done = 0
        titles = []
        for i in search1:
            for key, value in i.items():
                if key == 'userId' and value == int(sys.argv[1]):
                    Max += 1
                    for key, value in i.items():
                        if key == 'completed' and value is True:
                            Done += 1
                            titles.append(i['title'])
        c = 0
        with open('{}.json'.format(int(sys.argv[1])), 'w+') as f:
            f.write('{')
            f.write('"{}": ['.format(int(sys.argv[1])))
            for i in search1:
                for key, value in i.items():
                    if key == 'userId' and value == int(sys.argv[1]):
                        c += 1
                        f.write(json.dumps({'task': i['title'],
                                            'completed': i['completed'],
                                            'username': usern}))
                        if c != Max:
                            f.write(", ")
            f.write(']}')