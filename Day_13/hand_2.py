import requests


post_url = "https://jsonplaceholder.typicode.com/posts"

# post
weather_data ={
    "City":"New york",
    'Temp':28,
    'humidity':60,
    'condition':"sunny"
}
def post(post_url,weather_data):
    response = requests.post(post_url,json=weather_data)

    if response.status_code == 201:
        print("user sucessfully created")
        response_data = response.json()
        print('response data',response_data)
post(post_url,weather_data)
