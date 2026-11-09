import requests

response = requests.get("https://api.github.com", timeout=5)
# if there is no response from the server within 5 seconds then the program will give an error