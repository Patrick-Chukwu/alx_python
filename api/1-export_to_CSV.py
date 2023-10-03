import requests
import sys
import csv

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

    # Create a CSV file for the employee
    csv_file_name = f'{user_id}.csv'

    with open(csv_file_name, mode='w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        # Write TODO list data to the CSV file
        for todo in todos_data:
            task_completed_status = todo['completed']
            task_title = todo['title']
            writer.writerow({
                'USER_ID': user_id,
                'USERNAME': username,
                'TASK_COMPLETED_STATUS': str(task_completed_status),
                'TASK_TITLE': task_title
            })

    print(f"Data exported to {csv_file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
