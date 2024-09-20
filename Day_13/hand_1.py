import requests

def region_code():
    try:
        response = requests.get("https://restcountries.com/v3.1/all")
        response.raise_for_status()  # Check for HTTP errors

        countries = response.json()

        for country in countries:
            name = country.get('name', {}).get('common', 'N/A')
            capital = country.get('capital', ['N/A'])[0]
            area = country.get('area', 'N/A')
            currency_code = country.get('currencies', {}).get('COP', {}).get('symbol', 'N/A')

            if currency_code == "$":
                print(f"Country: {name}")
                print(f"Capital: {capital}")
                print(f"Area: {area}")
                print(f"Currency Code: {currency_code}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data: {e}")

region_code()