import requests
import sys
import json

def get_employee_info(employee_id):
    # Define the base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Create the URL for the employee's TODO list
    todos_url = f'{base_url}/users/{employee_id}/todos'

    # Send a GET request to retrieve TODO list data
    todos_response = requests.get(todos_url)

    if todos_response.status_code != 200:
        print("Error: Unable to retrieve TODO list data.")
        return

    # Create the URL for the employee's details
    details_url = f'{base_url}/users/{employee_id}'

    # Send a GET request to retrieve employee details
    details_response = requests.get(details_url)

    if details_response.status_code != 200:
        print("Error: Unable to retrieve employee details.")
        return

    # Parse the JSON responses
    todos_data = todos_response.json()
    details_data = details_response.json()

    # Extract employee information
    user_id = details_data.get('id', 'Unknown')
    username = details_data.get('username', 'Unknown')

    # Create a JSON file for the employee
    json_file_name = f'{user_id}.json'

    employee_data = {str(user_id): []}

    # Build the JSON data for tasks
    for todo in todos_data:
        task_data = {
            "task": todo['title'],
            "completed": todo['completed'],
            "username": username
        }
        employee_data[str(user_id)].append(task_data)

    with open(json_file_name, 'w') as json_file:
        json.dump(employee_data, json_file)

    print(f"Data exported to {json_file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
