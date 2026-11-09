import requests

def get_github_user(username):
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        print(f"Name: {data['name']}")
        print(f"Public repos: {data['public_repos']}")
        print(f"Followers: {data['followers']}")
    except requests.exceptions.RequestException as e:
        print("Error:", e)

name = input("GitHub username daalo: ")
get_github_user(name)