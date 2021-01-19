import scrapy

from scrapy.loader import ItemLoader
from w3lib.html import remove_tags

from ..items import AksakovoItem
from scrapy.linkextractors import LinkExtractor

class NikkeiSpider(scrapy.Spider):
	name = 'aksakovo2'

	start_urls = ['http://aksakovo.bg/section-90-content.html']

	def parse(self, response):
		post_links = response.xpath('//div[@class="new-item-learn-more"]/a/@href')
		print(post_links)
		yield from response.follow_all(post_links, self.parse_post)

		pagination_links = response.xpath('//div[@class="pages-top light-theme simple-pagination"]/ul/li/a[@class="page-link next"]/@href')
		yield from response.follow_all(pagination_links, self.parse)

	def parse_post(self, response):

		title = response.xpath('//h1/text()').get()
		print(title)
		description = response.xpath('//div[@class="new-item-block-content"]').getall()
		if description:
			description = remove_tags(str(description[0])).strip()

		item = ItemLoader(item=AksakovoItem(), response=response)
		item.add_value('title', title)
		item.add_value('description', description)

		return item.load_item()
