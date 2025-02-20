Hello Guys
CortexCrawler is a Scrapy-based web scraping tool designed to navigate through websites and gather structured data.
It uses custom rules to follow links and scrape specific content like titles, prices, and availability.
The extracted information is then stored in JSON format for easy access and analysis.

WARNING *****: Use the code only in scrapable websites,  
               Do not use it in any reputed websites e.g. Amazon, YouTube.  
               If you want to scrape data from these sites, make sure you use a proper VPN.  
               ***Otherwise, your IP may be blocked from accessing those sites permanently.***

Follow the steps:   WINDOWS ONLY
1-->Go to CMD on windows and give : pip install scrapy
2--->Go to Vscode and open the folder/directory which you want to work in
3-->open the terminal and give : scrapy startproject project_name
4-->use the code in the cortexcrawler.py file and initialize it inside the spiders folder
5-->navigate to the current folder which is CortexCrawler/CortexCrawler in my case
6-->run the command : scrapy crawl name_of_your_crawer (mycrawler in my case)
7-->To save it readable format: scrapy crawl name_of_your_crawer (mycrawler in my case) -o output.json
8-->The scrapped data will be stored in output.json file



->scrapy shell web_url: in terminal to access individual contents
    #then: response.css("h1")
    #display html code for particular part: response.css("h1").get()
    #response.css("h1::text").get()
    #response.css("h1::text").getall(): to get all the links

->To run
->cd CortexCrawler/CortexCrawler  scrapy crawler crawler_name -o ouput.json

->Time complexity O(N) where N is Number of pages crawled

    1. **Number of Pages Crawled**: The spider follows two types of links—category pages and individual book pages. Each category page might link to multiple book pages. The total number of pages depends on how many categories there are and how many books per category. If there are C categories and B books per category, the total pages could be roughly C + B*C. But in reality, it's a tree structure, so maybe it's more like O(N), where N is the total number of pages.

    2. **Processing Per Page**: For each page, especially book pages, the spider extracts data using CSS selectors. The parsing functions are straightforward, so each parse operation is O(1) since it's a fixed number of operations per page. However, if the number of elements per page varied a lot, it might be different, but here it's fixed fields.

    3. **Network Latency**: Web scraping is I/O bound because the time is mostly spent waiting for network responses. Time complexity in Big O usually focuses on computational steps, not I/O. But the user might be interested in how the number of pages affects total time, which would be linear in terms of pages crawled, assuming each page takes roughly the same time to fetch and parse.

        If the spider crawls 100 pages:
        100 network requests (O(N)).
        100 parse operations (O(N)).
        Total time ≈ 100 × (network delay + parsing time).


Time required to execute before optimizing: 113.782346 sec, 118.640294 sec
After addding concurrency, optimizing link extracter, using pipelines: 72.012254 sec, 67.112196 sec
After Cache responses to prevent re-downloading same content(in seetings.py) : 7.68 sec
