#!/usr/bin/python3
"""
Summarize an employee's TODO list and write it to a file as JSON
"""
from argparse import ArgumentParser
from json import dump
from os import path
from requests import get
from sys import argv

USERS = 'https://jsonplaceholder.typicode.com/users'
TODOS = 'https://jsonplaceholder.typicode.com/todos'

if __name__ == '__main__':
    parser = ArgumentParser(prog=path.basename(argv[0]))
    parser.add_argument('id', type=int, help='employee ID')
    args = parser.parse_args()
    user = get('/'.join([USERS, str(args.id)])).json()
    with open('.'.join([str(args.id), 'json']), 'w') as ostream:
        dump({
            str(args.id): [{
                "task": task['title'],
                "completed": task['completed'],
                "username": user['username'],
            } for task in get(TODOS, params={'userId': args.id}).json()]
        }, ostream)
