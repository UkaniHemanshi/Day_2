from urllib.parse import urlparse, parse_qs, urlencode

url = "https://www.example.com/path/to/resource?search=python&lang=en"

parsed_url = urlparse(url)
print(f"Domain: {parsed_url.netloc}")
print(f"Path: {parsed_url.path}")
print(f"Query: {parsed_url.query}")

url = "https://www.example.com/search?query=python$sort=recent"
parsed_url = urlparse(url)
query_params = parse_qs(parsed_url.query)
print(f"Query params:{query_params}")

base_url = "https://www.example.com/search"
query_params = {'query':'Python','sort':'recent'}
updated_url = f"{base_url}?{urlencode(query_params)}"
print(f"Updated Url:{updated_url}")

