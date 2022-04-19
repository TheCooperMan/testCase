# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
import csv

from .constants import *

TOP_X = 50


class TestcasePipeline:

    def __init__(self):
        self.con = sqlite3.connect('brands.db')
        self.cur = self.con.cursor()
        self.creat_table()

    def creat_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS brand (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            brand_contact_url VARCHAR ,
                            brand_name VARCHAR,
                            total_products INTEGER,
                            total_sells INTEGER,
                            total_likes INTEGER,
                            is_top_seller BOOLEAN NOT NULL CHECK (is_top_seller IN (0 , 1)),
                            location VARCHAR,
                            rating REAL,
                            score REAL 
                        );""")

    def process_item(self, item, spider):
        sql = 'INSERT INTO brand (brand_contact_url, brand_name, total_products, total_sells, total_likes, is_top_seller, location, rating, score) values(?, ?, ?, ?, ?, ?, ?, ?, ?)'
        self.cur.execute(sql, tuple(item.values()))
        self.con.commit()

        return item

    def close_spider(self, spider):
        self.get_top_x()

    def get_top_x(self):
        sql = 'SELECT * FROM brand order by brand.score desc limit {}'.format(TOP_X)
        self.cur.execute(sql)
        results = self.cur.fetchall()

        header = ['id', BRAND_CONTACT_URL, BRAND_NAME, TOTAL_PRODUCTS, TOTAL_SELLS, TOTAL_LIKES, IS_TOP_SELLER, LOCATION, RATING, SCORE]

        with open('top_{}_brands.csv'.format(TOP_X), 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            # write the header
            writer.writerow(header)
            for row in results:
                # write the data
                writer.writerow(row)
