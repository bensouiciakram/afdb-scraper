# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# data container 
class AfdbItem(scrapy.Item):

    url = scrapy.Field()
    title = scrapy.Field()
    brand = scrapy.Field()
    description = scrapy.Field()
    category = scrapy.Field()
    image_urls = scrapy.Field()
    sku = scrapy.Field()
    type = scrapy.Field()
    finition = scrapy.Field()
    #additional req
    stock = scrapy.Field()


    details = scrapy.Field()


    # done
    variure = scrapy.Field()


