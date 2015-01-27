# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from tutorial.items import DmozItem
from scrapy.http import Request,FormRequest
from scrapy.selector import HtmlXPathSelector
#from scrapy.spider import BaseSpider
#import MySQLdb
class DmozSpider(scrapy.Spider):
    name = "dmoz"
    #allowed_domains = ["zdnet.com"]
    allowed_domains = ["2cto.com"]
    start_urls = [
        #"http://security.zdnet.com.cn//"
        "http://www.2cto.com/News/"
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]
#    def GetUrls(self,num):
#            db = MySQLdb.connect("localhost","root","lcy492","security",charset='utf-8')
#            cursor = db.cursor()
#            urls = []
#            sql = "select link from security.dmoz oder by id limit %s"%(num)
#            try:
#                cursor.execute(sql)
#                data = cursor.fetchall()
#                for row in data:
#                    link = row[0]
#                    url = "http://....."%link
#                    urls.append(url)
#            except:
#                print "Error: unable to fetch data"
#            else:
#                return urls
#        
    def parse(self,response):
        #print response.body
        sel = Selector(response)
        item = DmozItem()
        #item['title'] =sel.xpath('//h3/a/text()').extract()
        #item['link'] = sel.xpath('//h3/a/@href').extract()
        item['title'] =sel.xpath('//ul/li/a/text()|//ul/li/h3/a/text()').extract()
        item['link'] = sel.xpath('//ul/li/a/@href|//ul/li/h3/a/@href').extract()
        #for page_url in sel.xpath('//h3/a/@href').extract():
        for page_url in sel.xpath('//ul/li/a/@href|//ul/li/h3/a/@href').extract():
            #print page_url
            yield Request(page_url,callback=self.parse_page)
        
        yield item
        
        
    def parse_page(self, response):
        
        sel = Selector(response)
        #print sel
        item = DmozItem()
        #item['time']=sel.xpath('//div[@class="qu_zuo"]/p[position()<2]/text()').extract()
        #item['content'] =sel.xpath('//div[@class="qu_ocn"]/p/text()').extract()
        item['content'] =sel.xpath('//dd[@id="Article"]/div/text()|//dd[@id="Article"]/p/text()|//p/text()').extract()
        item['time']=sel.xpath('//dd[@class="frinfo line_blue"]/text()').extract()
        yield item
    
     
    
    