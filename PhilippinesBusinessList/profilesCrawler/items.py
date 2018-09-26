# -*- coding: utf-8 -*-
import scrapy

class ProfileItem(scrapy.Item):
    CreatedOn = scrapy.Field()
    CompanyName = scrapy.Field()
    CompanyUrl = scrapy.Field()
    CompanyPhoto = scrapy.Field()
    CompanyStreet = scrapy.Field()
    CompanyCity = scrapy.Field()
    CompanyState = scrapy.Field()
    Country = scrapy.Field()
    CompanyDesc = scrapy.Field()
    PhoneNumber = scrapy.Field()
    EmployeeSize = scrapy.Field()
    Industry = scrapy.Field()
    FoundedOn = scrapy.Field()
    CompanyWeb = scrapy.Field()
    ContactPerson = scrapy.Field()
    CompanyManager = scrapy.Field()
    ContactInfo = scrapy.Field()

