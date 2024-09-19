import  scrapy

class Bookspider(scrapy.Spider):
    name = 'A3PageSpider'
    start_urls = ['https://books.toscrape.com/']
    def parse(self, response):
        # links of the page
        page_links = response.css('a::attr(href)').getall()

        #print the page links for debugging purpose
        print(f"Page links : {page_links}")
        for page_link in page_links:
            yield {
                'page_links': page_link
            }

        # next_page = response.css('a::attr(href)').getall()
        # if next_page is not None:
        #     next_page_url = response.urljoin(next_page)
        #     yield scrapy.Request(url=next_page_url, callback=self.parse)