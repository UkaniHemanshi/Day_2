import requests

# send a get request
response = requests.get("https://restcountries.com/v3.1/all")

# check the status code
if response.status_code == 200:
    # print the response content
    print("Response recieved")
    # print(response.json())
else:
    print('Failed to retrieve data:', response.status_code)
countries = response.json()

# loop through the list of countries and display relevant info
for country in countries:
    name = country.get('name',{}).get('common','N/A')
    capital = country.get('capital',['N/A'])[0]
    area = country.get('area','N/A')
    if name == "India":
        print(f"Country:{name}")
        print(f"Capital:{capital}")
        print(f"Area:{area}")
