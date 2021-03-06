import scrapy 

class StackSpider(scrapy.Spider):
	name = "stack"
	start_urls = [
		"http://stackoverflow.com/questions?pagesize=50&sort=newest",
		]
	def parse(self,response):
		for question in response.xpath('//div[@class="summary"]/h3'):
			yield {
				'title': question.xpath('a[@class="question-hyperlink"]/text()').extract()[0],
            	'url' :  question.xpath('a[@class="question-hyperlink"]/@href').extract()[0],
        	}
		page_number = response.xpath('//span[@class="page-numbers current"]/text()').extract_first()
		page_number = str(int(page_number)+1)
		next_page = response.urljoin('questions?page='+page_number+'&sort=newest')
		print page_number
		if page_number is not None:
			yield scrapy.Request(next_page,callback=self.parse,dont_filter=True)


