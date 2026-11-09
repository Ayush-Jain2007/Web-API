import requests

new_post = {"title": "Hello", "Body": "My First Post", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
print(response.status_code)
print(response.json())