import requests
import sys

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

    # Extract employee name
    employee_name = details_data.get('name', 'Unknown Employee')

    # Calculate the number of completed tasks and total tasks
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])
    total_tasks = len(todos_data)

    # Display employee TODO list progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")

    # Display titles of completed tasks
    for todo in todos_data:
        if todo['completed']:
            print(f"     {todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
