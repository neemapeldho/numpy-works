import requests

url = "https://dummyjson.com/products"

response = requests.get(url)

print(response)

print(response.json())

print(response.status_code)   # like 404 error upto 400 ok above request error