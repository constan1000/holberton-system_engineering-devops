#!/usr/bin/python3
"""
Summarize an employee's TODO list progress
"""
from argparse import ArgumentParser
from os import path
from requests import get
from sys import argv

API = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':

    parser = ArgumentParser(prog=path.basename(argv[0]))
    parser.add_argument('id', type=int, help='employee ID')
    args = parser.parse_args()
    user = get('/'.join([API, 'users', str(args.id)])).json()
    todo = get('/'.join([API, 'todos']), params={'userId': args.id}).json()
    completed = [task for task in todo if task['completed'] is True]
    print('Employee {} is done with tasks({}/{}):'.format(
        user['name'], len(completed), len(todo)))
    print('\n'.join('\t {}'.format(task['title']) for task in completed))
