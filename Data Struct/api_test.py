import requests

url = "https://api.thecatapi.com/v1/images/search"
response = requests.get(url)

print(response.status_code)

data = response.json()
print(data)