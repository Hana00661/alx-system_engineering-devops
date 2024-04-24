#!/usr/bin/python3

"""Script to export data in the JSON"""

if __name__ == "__main__":

    import json
    import requests
    from sys import argv

    url_user = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    url_todos = url_user + '/todos'

    response_user = requests.get(url_user)
    name = response_user.json()['username']

    all_tasks = requests.get(url_todos).json()

    list_tasks = []

    for task in all_tasks:
        task_dict = {
            "task": task['title'],
            "completed": task['completed'],
            "username": name
        }
        list_tasks.append(task_dict)

    json_object = json.dumps({argv[1]: list_tasks})

    with open("{}.json".format(argv[1]), 'w') as file:
        file.write(json_object)
