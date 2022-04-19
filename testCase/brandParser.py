import re


class BrandParser:
    def __init__(self, response):
        self.response = response

    def get_brand_name(self):
        return self.response.xpath('//h1[contains(@class,"wt-text-heading-01")]/text()').get()

    def get_brand_contact_url(self):
        return self.response.url

    def get_total_products(self):
        total_products = self.response.xpath('//ul[contains(@class,"wt-tab")]/button/span[2]/text()').get()
        return int(total_products) if total_products else 0

    def get_total_sells(self):
        if self.response.css('.shop-sales-reviews > span.wt-text-caption a::text'):
            sells = self.response.css('.shop-sales-reviews > span.wt-text-caption a::text').get(default=0)
        else:
            sells = self.response.css('.shop-sales-reviews > span.wt-text-caption.wt-no-wrap::text').get(default=0)
        sells = re.findall(r'[\d]*[.,\d]+', sells)[0].replace(',', '') if sells !=0 else 0
        return int(sells)

    def get_total_likes(self):
        likes = self.response.xpath('//a[contains(@href, "favoriters")]/text()').get(default=0)
        return int(likes) if likes == 0 else int(likes.split()[0])

    def get_is_top_seller(self):
        return self.response.xpath('//div[contains(@class,"star-seller-badge")]').get() is not None

    def get_location(self):
        return self.response.xpath('//span[contains(@class,"shop-location")]/text()').get()

    def get_rating(self):
        return float(self.response.xpath('//input[contains(@name,"rating")]/@value').get(default=0))
