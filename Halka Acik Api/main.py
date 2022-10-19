import requests
response = requests.get("https://dog.ceo/api/breeds/image/random")
print(response.json())