import scrapy
from lxml import html
import pdb
import scrapy_splash
from scrapy.loader import  ItemLoader
from tutorial.items import Restraunt
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
class QuotesSpider(scrapy.Spider):
	name="zom_B"
	def start_requests(self):
		urls=['https://www.zomato.com/patna/delivery']

		for url in urls:
			yield scrapy.Request(url=url,callback=self.parse)
	def parse(self,response):
		restrauntList=response.css("div.card .content")
		
		for eachRestraunt in restrauntList:
			r=Restraunt()
			lnk=eachRestraunt.css("a.bold::attr(href)").extract_first()
			r["Link"]=eachRestraunt.css("a.bold::attr(href)").extract_first()
			r["typ"]=eachRestraunt.css(".fontsize6::text").extract()
			r["Address"]=eachRestraunt.css(".ln22::text").extract_first() 
			r["Rating"]=eachRestraunt.css("div.rating-popup::text").extract_first()
			r["ZID"]=eachRestraunt.css("div.rating-popup::attr(data-res-id)").extract_first()
			r["Locality"]=eachRestraunt.css("b::text").extract_first()
			r["Name"]=eachRestraunt.css(".ln24::text").extract_first()
			yield scrapy.Request(url=lnk+'/info', callback=self.parse_order, meta={'item':r})
			
		nextpage=response.css(".next::attr(href)").extract_first()
		if nextpage is not None:
			yield response.follow(nextpage, callback=self.parse)	
	
	def parse_phone(self,response):
		for items in response.css("div.ui.segment.category-container"):
			 res=response.meta["item"]
			 category=items.css("h3::text").extract()[0]
			 item=items.css(".header::text").extract()
			 res["price"]=items.css(".description::text").extract()
			 Price=[]
			 for r in  res["price"]:
			 	val=r.encode("ascii","ignore")
			 	if len(val)>0 and val !=" " and val !="onwards":
			 		Price.append(val)
			 res["price"]=Price
			 res["category"]=category
			 res["item"]=item
			 yield res
		#yield item
	def parse_order(self,response):
		item=response.meta['item']
		item["Phone"]=response.css(".tel::attr(aria-label)").extract()
		yield scrapy.Request(url=item["Link"]+'/order', callback=self.parse_phone, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 20}
                    
                },
                'item':item
            })
		
		#yield scrapy.Request(url=item["Link"]+"/info",callback=self.parse_order,meta={'item':item})
		#yield item	
		#options = Options()
        #options.add_argument("--headless")
       # browser=webdriver.Firefox()
        #browser.get(response.url)
        #time.sleep(10)
    #    htm = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
     #   tree=html.fromstring(htm)
      #  print tree
