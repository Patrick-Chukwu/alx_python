import requests

r = requests.get('https://api.github.com/events')
print(r.status_code)

p = requests.post('https://httpbin.org/post', data={'Name': 'Patrick'})
print(p.status_code)



"""copy"""
username = "Patrick-Chukwu"
token = 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
url = "https://api.github.com/user"

response = requests.get(url, auth=(username, token))

if response.status_code == 200:
    user_data = response.json()
    print("Your GitHub ID:", user_data["id"])
else:
    print("Error:", response.text)
