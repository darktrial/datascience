import scrapy
from pttmobile.items import PttmobileItem


class PttMobileSpider(scrapy.Spider):
    name = "pttmobile"
    start_urls = [
        'https://www.ptt.cc/bbs/MobileComm/index.html',
    ]
    allowed_domains = ["ptt.cc"]
    visit_pages=0
    page_count=60
    def parse_detail(self, response):
        item = response.meta['item']
        item['content']=response.xpath("//div[contains(@id,'main-content')]/text()").extract()
        positive_user=[]
        negative_user=[]
        for quote in response.css('div.push'):
            if ('噓' in quote.xpath("span[contains(@class,'push-tag')]/text()")[0].extract()):
                username=quote.xpath("span[contains(@class,'push-userid')]/text()")[0].extract()
                if (username not in negative_user):
                    negative_user.append(username)
            else:
                username=quote.xpath("span[contains(@class,'push-userid')]/text()")[0].extract()
                if (username not in positive_user):
                    positive_user.append(username)
        item['positive_user']=positive_user
        item['negative_user']=negative_user
        yield item
    
    def parse(self, response):
        if (self.visit_pages > self.page_count): 
            return
        itemlist=[]
        for quote in response.css('div.r-ent'):
            title_list=list(quote.xpath("div[contains(@class,'title')]/text()"))
            if (len(title_list)<2):
                continue
                #if (('公告' in quote.xpath("div[contains(@class,'title')]/a/text()")[0].extract() ) or ('已被刪除' in quote.xpath("div[contains(@class,'title')]/a/text()")[0].extract())):
                    #continue
            #else:
                #continue
            item=PttmobileItem()
            item['positive_count']=quote.xpath("div[contains(@class,'nrec')]/span[contains(@class,'f2') or contains(@class,'f3')]/text()").extract_first()
            if (item['positive_count']==None):
                item['positive_count']='0'
            item['negative_count']=quote.xpath("div[contains(@class,'nrec')]/span[contains(@class,'f0')]/text()").extract_first()
            if (item['negative_count']==None):
                item['negative_count']='0'
            item['title']=quote.xpath("div[contains(@class,'title')]/a/text()").extract()
            item['content_url']=quote.xpath("div[contains(@class,'title')]/a/@href").extract_first()
            item['date']=quote.xpath("div[contains(@class,'meta')]/div[contains(@class,'date')]/text()").extract_first()
            item['author']=quote.xpath("div[contains(@class,'meta')]/div[contains(@class,'author')]/text()").extract_first()
            
            
            itemlist.append(item)
               
        
        for myitem in itemlist:
            next_page = response.urljoin(myitem['content_url'])
            yield scrapy.Request(next_page,meta={'item': myitem} ,callback=self.parse_detail)
            
        #print(itemlist)    
        #return itemlist    
        
        prev_page=response.urljoin(response.xpath("//div[contains(@class,'btn-group-paging')]/a/@href")[1].extract())
        print("the prev page"+prev_page)
        self.visit_pages=self.visit_pages+1
        yield scrapy.Request(prev_page,callback=self.parse)
        

        #next_page = response.css('li.next a::attr("href")').extract_first()
        #if next_page is not None:
        #    next_page = response.urljoin(next_page)
        #    yield scrapy.Request(next_page, callback=self.parse)


