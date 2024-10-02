import requests
import datetime

USERNAME = "carduibot"
TOKEN = "dq4e78G95%9i3h"
GRAPH_ID = "habits1"

pixela_endpoint = "https://pixe.la/v1/users"

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%M%D"),
    "quantity": "5",
}

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

"""
### Create User

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

### Create a graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Tracker",
    "unit": "pages",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
"""


