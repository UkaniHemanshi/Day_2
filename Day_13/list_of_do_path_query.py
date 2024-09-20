from urllib.parse import urlparse, parse_qs, urlencode

urls = ["https://www.example.com/path/to/resource?search=python&lang=en","https://www.shop.com/products/item?id=123&color=blue","https://news.site.com/world/asia?date=2024-09-16&author=JohnDoe","https://blog.example.org/articles/tech?tag=AI&year=2024"]
for url in urls:
    parsed_url = urlparse(url)
    print(f"Domain: {parsed_url.netloc}")
    print(f"Path: {parsed_url.path}")
    print(f"Query: {parsed_url.query}")
    print("\n")