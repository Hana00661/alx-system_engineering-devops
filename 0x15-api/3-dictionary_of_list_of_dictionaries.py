#!/usr/bin/python3

"""Script to export data in the JSON"""

if __name__ == "__main__":

    import json
    import requests
    from sys import argv

    url_user = 'https://jsonplaceholder.typicode.com/users/'
    filename = 'todo_all_employees.json'
    all_users = requests.get(url_user).json()
    dico = {}

    for user in all_users:
        name = user['username']
        user_id = user['id']

        url_todos = url_user + str(user_id) + '/todos'
        all_tasks = requests.get(url_todos).json()

        list_tasks = []

        for task in all_tasks:
            task_dict = {
                "task": task['title'],
                "completed": task['completed'],
                "username": name
            }
            list_tasks.append(task_dict)
        dico[user_id] = list_tasks
    json_object = json.dumps(dico)

    with open(filename, 'w') as file:
        file.write(json_object)
