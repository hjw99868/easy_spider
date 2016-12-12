import scrapy

from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from tutorial.items import DmozItem
import sys

class DmozSpider(CrawlSpider):
    name = "dmoz"
    allowed_domains=["movie.douban.com"]
    start_urls=["https://movie.douban.com/top250"]
    reload(sys)
    sys.setdefaultencoding('utf8')
    rules=(
        Rule(SgmlLinkExtractor(allow=(r'https://movie.douban.com/subject/\d{7}')),callback="parse_item"), 
        Rule(SgmlLinkExtractor(allow=(r'https://movie.douban.com/top250\?start=\d+.*'))),
    )
  
    def parse_item(self, response):
            sel=Selector(response)
            item = DmozItem()
            item['num'] = sel.xpath('//*[@id="content"]/div[1]/span[1]/text()').extract()
            item['filmname'] = sel.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
            item['director'] = sel.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract()
            item['genre'] = sel.xpath('//*[@id="info"]/span[@property="v:genre"]/text()').extract()
            item['score'] = sel.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract()
            item['link'] = response.url
            item['year']=sel.xpath('//*[@id="content"]/h1/span[2]/text()').re(r'\((\d+)\)')
            item['commentnum'] = sel.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()').extract()
            item['picture']= sel.select('//*[@id="mainpic"]/a/img/@src').extract()
            item['actor']= sel.xpath('//a[@rel="v:starring"]/text()').extract()
            storr=sel.xpath('//*[@id="link-report"]/span[1]/text()|//*[@id="link-report"]/span[1]/span/text()').extract()
            strr="".join(storr)
            item['story']=''.join(strr.split())
            return item
