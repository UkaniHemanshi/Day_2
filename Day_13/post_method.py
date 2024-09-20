import requests
post_url = "https://reqres.in/api/users"

# post
post_data ={
    "name":"hemanshi",
    "job":"IT"
}

response = requests.post(post_url,json=post_data)

if response.status_code == 201:
    print("user sucessfully created")
    response_data = response.json()
    print('response data',response_data)