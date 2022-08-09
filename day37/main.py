import requests
from datetime import datetime

USERNAME = "grendach"
TOKEN = "gq049u5nhql;nm=1-09497y"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# # Create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# # Create graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# # Add pixels to graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "14",
}

# response = requests.post(url=graph_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# # Update pixels from graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20220620"
new_pixel_data = {
    "quantity": "0",
}
# response = requests.put(url=graph_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# # Delete pixels from graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20220809"

response = requests.delete(url=graph_endpoint, headers=headers)
print(response.text)
