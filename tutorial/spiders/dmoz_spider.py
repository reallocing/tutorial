# -*- coding: utf-8 -*-
#encoding=utf-8
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
import scrapy
from scrapy.selector import Selector
from tutorial.items import DmozItem
from scrapy.http import Request,FormRequest
from scrapy.selector import HtmlXPathSelector
import mysql.connector

#from scrapy.spider import BaseSpider
#import MySQLdb
class DmozSpider(scrapy.Spider):
    name = "dmoz"
    #allowed_domains = ["zdnet.com"]
    #allowed_domains = ["2cto.com"]
    start_urls = ["http://www.2cto.com/News/"]
		
    def start_requests(self):
	    #括号里数字是每次要取的url数目
		urls = self.getUrls(4)
		print urls
		for url in self.start_urls:
			yield Request(url)
			
    def getUrls(self,num):
		    
           db = mysql.connector.connect(user="root",password="123456",database="security")
		   
           cursor = db.cursor()
           urls = []
		   
           sql = "select link from security.link order by id limit %s"%(num)
           try:
               cursor.execute(sql)
               data = cursor.fetchall()
               for row in data:
					print "row:"
					print row  
					urls.append(row)
           except:
               print "Error: unable to fetch data"
           else:
               return urls
       
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
    
     
    
    