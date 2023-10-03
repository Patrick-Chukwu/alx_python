import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python3 3-dictionary_of_list_of_dictionaries.py")
        sys.exit(1)

    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    try:
        response_users = requests.get(url_users)
        response_todos = requests.get(url_todos)

        users = response_users.json()
        todos = response_todos.json()

        # Create a dictionary to store tasks for each user
        user_tasks = {}

        for user in users:
            user_id = user['id']
            username = user['username']

            # Filter todos for the current user
            user_todos = [todo for todo in todos if todo['userId'] == user_id]

            # Create a list of task dictionaries for the user
            tasks = [{'username': username, 'task': todo['title'], 'completed': todo['completed']} for todo in user_todos]

            # Add the tasks list to the user_tasks dictionary
            user_tasks[user_id] = tasks

        # Create a JSON file with all tasks
        with open('todo_all_employees.json', 'w') as json_file:
            json.dump(user_tasks, json_file)

        print("Data exported to todo_all_employees.json")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
