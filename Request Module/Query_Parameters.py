import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url, params={"userId": 1})
print(response.url)               # .../posts?userId=1
print(len(response.json()))       # sirf user 1 ki posts