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
