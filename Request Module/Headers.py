import requests

headers = {
    "User-Agent": "NaviFreight",
    "Authorization": "bearer YOUR_TOKEN"
}
response = requests.get("https://api.github.com/user", headers=headers)

# don't use API KEY directly as it might get leak
# instead use

import os
api_key = os.getenv("MY_API_KEY")
headers = {"Authorization": f"bearer {api_key}"}