import requests
from datetime import datetime

USERNAME = "joelpaull123"
TOKEN = "bn28dhfji33jf"
GRAPH_ID = "graph1"
# Save API endpoint in URL
pixela_endpoint = "https://pixe.la/v1/users"


# Save required API parameters
user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# Returned response saved to variable     # user Created
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Coding Graph",
    "unit" : "Hours",
    "type" : "int",
    "color" : "sora"
    
}

headers = {
    "X-USER-TOKEN" : TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Get current date in correct format
date = datetime.now().strftime("%Y%m%d")

# Add a pixel to tracker

pixel_data = {
    "date" : date,
    "quantity" : "2"
}

graph_add_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
print(graph_add_endpoint)
# response = requests.post(url=graph_add_endpoint, json=pixel_data, headers=headers)


# Update pixel in tracker

update_pixel = {
    "quantity" : "5"
}

update_pixel_endpoint = f"{graph_add_endpoint}/20230504"
response = requests.put(url=update_pixel_endpoint, json=update_pixel, headers=headers)
print(response.text)


