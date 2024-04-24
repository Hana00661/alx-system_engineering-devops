#!/usr/bin/python3

""" Script that returns informations of employee"""

if __name__ == "__main__":

    import requests
    from sys import argv

    url_user = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    url_todos = url_user + '/todos'

    response_user = requests.get(url_user)
    name = response_user.json()['name']

    response_todos = requests.get(url_todos)
    all_tasks = response_todos.json()

    done_tasks = []

    for task in all_tasks:
        if task['completed'] is True:
            done_tasks.append(task)

    print("Employee {} is done with tasks({}/{}):".format
          (name, len(done_tasks), len(all_tasks)))

    for task in done_tasks:
        print('\t ' + task['title'])
