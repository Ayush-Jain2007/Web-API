import requests as req

# Get request
response = req.get("https://api.github.com/users/octocat")
print(response.status_code)

# Response object
print(response.text)         # raw text (string)
data = response.json()       # Converts JSON to Python dictionary
print(data["login"])         # octocat
print(data["public_repos"])  # Amount of repos
print(response.headers)      # extra info about server