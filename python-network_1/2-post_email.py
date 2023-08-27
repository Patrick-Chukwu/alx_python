"""Importing requests and sys and using it to post a mail to a url"""

import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]
data = {'email': email}

response = requests.post(url, data=data)

print(response.text)
