from urllib.parse import urlparse
# class URLShortner:
#     url_dict = {}
#
#     def add_url(self,original_url):
#         parsed_url = urlparse(original_url)
#         if original_url in self.url_dict:
#             print("Already exists in dictionary")
#             return self.url_dict[original_url]
#         else:
#             self.url_dict[original_url] = parsed_url.netloc
#             return self.url_dict
#
# obj1 = URLShortner()
# print(obj1.add_url("https://www.example.com/path/to/resource?search=python&lang=en"))

class URLShortner:
    url_dict = {}
    base_url = "http://short.url/"

    def add_url(self,original_url):
        if original_url in self.url_dict:
            print("Already exists in dictionary")
            print(self.url_dict[original_url])
        else:
            index = len(self.url_dict) + 1
            self.url_dict[original_url] = self.base_url + str(index)
            print(self.url_dict)

obj1 = URLShortner()

obj1.add_url("https://www.example.com/path/to/resource?search=python&lang=en")
obj1.add_url("https://www.example.com/search?query=python$sort=recent")
obj1.add_url("https://www.example.com/search?query=python$sort=recent")




