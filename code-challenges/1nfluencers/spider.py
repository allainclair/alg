import scrapy
from icecream import ic


class TwitterSpider(scrapy.Spider):
    name = 'twitter_spider'
    start_urls = ['https://twitter.com/search?q=influencer&src=typed_query&f=user']

    def parse(self, response):
        ic(response)
        ic(response.text)
        for div in response.xpath('//div[@data-testid = "cellInnerDiv"]'):
            ic(dir(div))
            ic(vars(div))
            yield {'div': div.css('::text').get()}

        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)

    # ./configure
    # make
    # make test
    # sudo make install
