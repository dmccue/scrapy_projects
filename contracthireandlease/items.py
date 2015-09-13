# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ContracthireandleaseItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    i_manufacturer = scrapy.Field()
    i_model = scrapy.Field()
    i_desc = scrapy.Field()
    i_contract_mileage = scrapy.Field()
    i_contract_term = scrapy.Field()
    i_contract_initial = scrapy.Field()
    i_contract_monthlyprice = scrapy.Field()
    i_url = scrapy.Field()
