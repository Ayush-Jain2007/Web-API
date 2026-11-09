import requests

try:
    response = requests.get("https://api.github.com/users/octocat", timeout=5)
    response.raise_for_status()   # 4xx/5xx status pe error uthata hai
    data = response.json()
    print(data["name"])

except requests.exceptions.Timeout:
    print("Server Timeout.")

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

except requests.exceptions.RequestException as e:
    print("Some other problem:", e)