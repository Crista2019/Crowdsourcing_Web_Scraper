# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrowdsourcingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    currencyType = scrapy.Field()
    campaignTitle = scrapy.Field()
    amountRaised = scrapy.Field()
    goal = scrapy.Field()
    endDate = scrapy.Field()
    numberContributors = scrapy.Field()
    story = scrapy.Field()
    url = scrapy.Field()
