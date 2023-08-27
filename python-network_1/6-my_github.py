"""Importing requests and sys to request from json api"""

import requests
import sys

if len(sys.argv) < 3:
    print("Usage: python script.py <username> <personal_access_token>")
    sys.exit(1)

username = sys.argv[1]
token = sys.argv[2]
url = "https://api.github.com/user"

response = requests.get(url, auth=(username, token))

if response.status_code == 200:
    user_data = response.json()
    print("Your GitHub ID:", user_data["id"])
else:
    print("Error:", response.text)
