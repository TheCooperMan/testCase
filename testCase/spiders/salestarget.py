import scrapy
from ..brandParser import BrandParser
from ..constants import *
from ..scoring import Scoring
from ..brand import Brand

NB_PAGES = 100


class SalesTarget(scrapy.Spider):
    name = "sales"

    def start_requests(self):
        for i in range(1, NB_PAGES):
            url = "https://www.etsy.com/fr/search/shops?ref=pagination&order=most_recent&page={}".format(i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        all_brands = response.xpath('//a[contains(@class,"wt-card")]/@href').getall()
        for url in all_brands:
            yield scrapy.Request(url=url, callback=self.parse_brand)

    def parse_brand(self, response):
        brand_parser = BrandParser(response)
        data = {}
        brand = Brand(brand_parser.get_brand_contact_url(),
                      brand_parser.get_brand_name(),
                      brand_parser.get_total_products(),
                      brand_parser.get_total_sells(),
                      brand_parser.get_total_likes(),
                      brand_parser.get_is_top_seller(),
                      brand_parser.get_location(),
                      brand_parser.get_rating())
        scoring = Scoring(brand)
        brand.set_score(scoring.get_score())

        data[BRAND_CONTACT_URL] = brand.brand_contact_url
        data[BRAND_NAME] = brand.brand_name
        data[TOTAL_PRODUCTS] = brand.total_products
        data[TOTAL_SELLS] = brand.total_sells
        data[TOTAL_LIKES] = brand.total_likes
        data[IS_TOP_SELLER] = brand.is_top_seller
        data[LOCATION] = brand.location
        data[RATING] = brand.rating
        data[SCORE] = brand.score

        yield data
