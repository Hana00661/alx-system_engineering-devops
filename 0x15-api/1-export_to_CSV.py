#!/usr/bin/python3

"""Script to export data in the CSV"""

if __name__ == "__main__":

    import csv
    import requests
    from sys import argv

    url_user = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    url_todos = url_user + '/todos'

    response_user = requests.get(url_user)
    name = response_user.json()['username']

    response_todos = requests.get(url_todos)
    all_tasks = response_todos.json()

    filename = argv[1] + '.csv'

    with open(filename, 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in all_tasks:
            writer.writerow([argv[1], name, task['completed'], task['title']])
