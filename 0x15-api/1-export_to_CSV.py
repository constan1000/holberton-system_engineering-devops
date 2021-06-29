#!/usr/bin/python3
""" Exporting information to CSV """
import csv
import requests
import sys
if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        res1 = requests.get('https://jsonplaceholder.typicode.com/todos')
        res2 = requests.get('https://jsonplaceholder.typicode.com/users')
        search1 = res1.json()
        search2 = res2.json()
        for y in search2:
            if y['id'] == int(sys.argv[1]):
                name = y['name']
                username = y['username']
        count = 0
        completed = 0
        titles = []
        for i in search1:
            for key, value in i.items():
                if key == 'userId' and value == int(sys.argv[1]):
                    count += 1
                    for key, value in i.items():
                        if key == 'completed' and value is True:
                            completed += 1
                            titles.append(i['title'])
        with open('{}.csv'.format(int(sys.argv[1])), 'w+') as f:
            writer = csv.writer(f, delimiter=',',
                                quotechar='"',
                                quoting=csv.QUOTE_ALL)
            for i in search1:
                for key, value in i.items():
                    if key == 'userId' and value == int(sys.argv[1]):
                        writer.writerow([int(sys.argv[1]),
                                         username, i['completed'],
                                         i['title']])