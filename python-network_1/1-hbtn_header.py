"""Importing requests and sys and using it to print a response
    """
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]
response = requests.get(url)

x_request_id = response.headers.get('X-Request-Id')
print(x_request_id)