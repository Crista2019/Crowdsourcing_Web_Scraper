# Croudsourcing Web Scraper
A small Python web-scraper based in Scrapy to crawl different crowdfunding campaigns for and animated films, write specific data to a file, and determine what common traits the most successful campaigns share. Much thanks to Toward Data Science for the awesome tutorial on building your own dataset using Scrapy, which helped me create this project.

## Running Web Crawler...
To run this program, make sure you have Scrapy framework installed,
navigate to *web_scraping\crowdsourcing*,
and run the command
`scrapy crawl my_scraper -o MonthDay_Year.json` or `scrapy crawl my_scraper -o MonthDay_Year.csv`

## To change info gathered...
Simply 1.) change the start URLs you are gathering data from, 
2.) increase the number of pages you want to scrape, and/or 
3.) use your browser (Firefox or Chrome) to inspect the elements you are scraping and change your xpath accordingly.

*In Fundrazr_scrape.py:*

````python	
class Fundrazr(scrapy.Spider):
	name = "my_scraper"
	
    # 1.
	start_urls = ["https://fundrazr.com/find?search=films%20and%20animation"]

	npages = 2

    # 2.
	for i in range(2, npages + 2):
		start_urls.append("https://fundrazr.com/find?search=films%20and%20animation&page=" + str(i))

	def parse(self, response):
    # 3.
		for href in response.xpath("//h2[contains(@class, 'title headline-font')]/a[contains(@class, 'campaign-link')]//@href"):
			# add the scheme, eg http://
			url  = "https:" + href.extract()
			yield scrapy.Request(url, callback=self.parse_dir_contents)
	...
```
