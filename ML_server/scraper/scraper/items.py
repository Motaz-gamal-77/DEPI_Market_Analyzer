# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonscrapItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product = scrapy.Field()
    #Auther = scrapy.Field()
    price = scrapy.Field()
    review_body = scrapy.Field()
    helpful_votes = scrapy.Field()
    ratings = scrapy.Field()

