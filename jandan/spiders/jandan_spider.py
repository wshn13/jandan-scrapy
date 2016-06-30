import scrapy
from scrapy import optional_features
from jandan.items import JandanItem

optional_features.remove('boto')

class JandanSpider(scrapy.Spider):
    name = "jandan"
    allowed_domains = ["jandan.net"]
    start_urls = [
        "http://www.jandan.net/pic"
    ]

    def parse(self, response):
        for sel in response.xpath("/html/body//div[@id='comments']/ol//li//img"):
            url = sel.xpath("@src")
            if url:
                url = url.extract()[0]
            else:
                url = sel.xpath("@org_src").extract()[0]
            item = JandanItem()
            item['image_urls'] = [url, ]
            item['file_urls'] = [url, ]
            yield item
        nexturl = response.xpath("/html/body//a[@class='previous-comment-page']/@href")
        print nexturl
        if nexturl:
            url = response.urljoin(nexturl[0].extract())
            yield scrapy.Request(url, self.parse)
