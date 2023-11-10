import requests
from datetime import datetime

USERNAME = ""
TOKEN = ""
GRAPH_ID = "graph2"
pixela_endpoint = "https://pixe.la/v1/users"

headers = {
	"X-USER-TOKEN": TOKEN
}

### User creation

# user_params = {
# 	"token": USERNAME,
# 	"username": TOKEN,
# 	"agreeTermsOfService": "yes",
# 	"notMinor": "yes"
# }

# # response = requests.post(url=pixela_endpoint, json=user_params)
# # print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

### Graph creation

# graph_config = {
# 	"id": "graph2",
# 	"name": "Coding Graph",
# 	"unit": "Hours",
# 	"type": "int",
# 	"color": "ajisai"
# }

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

### Pixel modification

today = datetime(year=2023, month=11, day=9)

pixel_config = {
	"date": today.strftime("%Y%m%d"),
	"quantity": "6"
}

# response = requests.put(url=pixel_endpoint, json=pixel_config, headers=headers)
# print (response.text)

### Pixel updating with put() command

today_fixed = today.strftime("%Y%m%d")

print(today_fixed)

mini_graph = {
	"quantity": "7"
}

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_fixed}"

# response = requests.put(url=update_endpoint, json=mini_graph, headers=headers)
# print(response.text)

### Pixel deletion using delete()

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_fixed}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)