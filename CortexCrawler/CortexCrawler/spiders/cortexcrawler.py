from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import signals  # Import signals to use spider lifecycle hooks
import time

class WebScraper(CrawlSpider):
    name = "mycrawler"  # Assign name to the crawler
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]  # Website to scrape

    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),
        Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item")  # parse_item is a function
    )

    def __init__(self, *args, **kwargs):
        super(WebScraper, self).__init__(*args, **kwargs)
        self.start_time = None  # Initialize start time

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(WebScraper, cls).from_crawler(crawler, *args, **kwargs)
        # Connect the spider_opened and spider_closed signals to measure time
        crawler.signals.connect(spider.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_opened(self, spider):
        # Record the start time when the spider opens
        self.start_time = time.time()
        print(f"Spider opened at: {self.start_time}")

    def spider_closed(self, spider):
        # Record the end time when the spider closes
        end_time = time.time()
        elapsed_time = end_time - self.start_time  # Calculate elapsed time
        print(f"Spider closed at: {end_time}")
        print(f"Time taken to execute the program: {elapsed_time:.2f} seconds")

    def parse_item(self, response):
        yield {
            "title": response.css(".product_main h1::text").get(),
            "price": response.css(".price_color::text").get(),
            "availability": response.css(".availability::text").get().strip().replace("\n", "").replace(" ", "")
        }

