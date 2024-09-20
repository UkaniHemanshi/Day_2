import requests

delete_url = "https://reqres.in/api/users/{id}"

response = requests.delete(delete_url)

if response.status_code == 204:
    print(response)
    print("user successfully ")
else:
    print("failed to delete")