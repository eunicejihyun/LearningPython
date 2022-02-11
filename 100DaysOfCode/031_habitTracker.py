import requests as r
from datetime import datetime

USERNAME = "yourusername"
TOKEN = "yourtoken"

GRAPH_ID = "graph1"

headers = {
    "X-USER-TOKEN": TOKEN
}

# ############################ Creating User Account on Pixela
pixela_endpoint = "https://pixe.la/v1/users"

# PIXELA_PARAMS = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
#
# response = r.post(url=pixela_endpoint, json=PIXELA_PARAMS)
#
# print(response.text)

# ############################ Create a Definition Graph

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# GRAPH_PARAMS = {
#     "id": GRAPH_ID,
#     "name": "Meditation Tracker",
#     "unit": "min",
#     "type": "int",
#     "color": "ajisai",
# }
#
# response = r.post(url=graph_endpoint, json=GRAPH_PARAMS, headers=headers)
# print(response.text)

# ############################ Post value to the graph
value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"


today = datetime.now()
yesterday = datetime(year=2022, month=2, day=10)

# VALUE_PARAMS = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "15",
# }
#
# response = r.post(url=value_endpoint, json=VALUE_PARAMS, headers=headers)
# print(response.text)


# ############################ Update a Value Point
update_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"

UPDATE_PARAMS = {
    "quantity": "60"
}

response = r.put(url=update_value_endpoint, json=UPDATE_PARAMS, headers=headers)
print(response.text)

# ############################ Delete a Value Point

delete_endpoint = update_value_endpoint

response = r.delete(url=delete_endpoint, headers=headers)
print(response.text)