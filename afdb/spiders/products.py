import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from afdb.items import AfdbItem
from scrapy import Request 
from scrapy.shell import inspect_response


class ProductsSpider(CrawlSpider):
    name = 'products'
    allowed_domains = ['afdb.fr']
    start_urls = ['https://www.afdb.fr']

    
    rules = (              # rule to extract the product url
        Rule(LinkExtractor(allow=[r'.html$','SKU'],deny=['INTERSHOP']), callback='parse_item', follow=True),
    )


    def parse_item(self, response):
        if not ('SKU' in response.url) :
            return
        loader = ItemLoader(AfdbItem(),response)
        # extracting of the data fields
        # adding the url of the product 
        loader.add_value('url',response.url)
        loader.add_css('title','h1 span[itemprop=name]::text')
        loader.add_css('brand','div.product-brand img::attr(title)')
        loader.add_css('image_urls','div.swiper-wrapper img::attr(src)')
        loader.add_css('description', 'div#ProductTabDescription div::text')
        loader.add_xpath('category','//li[contains(@class,"breadcrumbs-list")][position()>1]/a/text()')
        loader.add_xpath('sku','(//span[@itemprop="sku"])[1]/text()')
        loader.add_value('details',self.get_details(response))
        loader.add_xpath('variure','//label[contains(text(),"VARIURE")]//parent::div/text()')
        loader.add_xpath('finition','//label[contains(text(),"FINITION")]//parent::div/text()')
        loader.add_xpath('type','//label[contains(text(),"TYPE")]//parent::div/text()')
        stock_url = 'https://www.afdb.fr/INTERSHOP/web/WFS/AFDB-B2B-Site/fr_FR/-/EUR/IncludeProduct-GetStocks?SKUs={}&ShowMessage=true'
        yield Request(
            stock_url.format(loader._values.get('sku')[0]),
            meta ={
                'loader':loader
            },
            callback=self.get_stock

        )


    def get_stock(self,response):
        loader = response.meta.get('loader')
        try:
            loader.add_value('stock',response.json()['results'][0]['views'][0]['result'][0]['message'])
        except Exception as e : 
            print(e)
            inspect_response(response, self)
        yield loader.load_item()
            

    def get_details(self,response):
        return {sel.xpath('.//dt//text()').get():sel.xpath('.//dd//text()').get() for sel in response.xpath('//dl[@class="ish-productAttributes"]')}
            