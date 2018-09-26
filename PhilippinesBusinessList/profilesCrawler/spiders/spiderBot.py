# -*- coding: utf-8 -*-
import scrapy, datetime, os, re
from profilesCrawler.items import ProfileItem

class SpiderbotSpider(scrapy.Spider):
    name = 'spiderBot'
    allowed_domains = ['www.businesslist.ph']
    alphabet = ['3','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z']
    start_urls = ["https://www.businesslist.ph/browse-business-directory/char:"+char for char in alphabet]

    def __init__(self):
        self.start_time = datetime.datetime.now().strftime("%Y-%m-%d")
        self.declare_xpath()

    def declare_xpath(self):
        self.allCategoriesUrlXPath = "//ul[@class='cat_list']/li//@href"
        self.allCompaniesUrlXPath = "//div[@class='company g_0']/h4//@href"
        self.nextPageUrlXPath = "//a[@rel='next']/@href"
        self.companyNameXPath = "//span[@id='company_name']/text()"
        self.companyPhotoXPath = "//a[@title='Company photo']//@href"
        self.companyStreetXPath = "//div[@class='text location']/text()"
        self.companyCityXPath = "//div[@class='text location']/a[contains(@class, 'city')]/text()"
        self.companyStateXPath = "//div[@class='text location']/a[contains(@class, 'state')]/text()"
        self.companyDescXPath = "//div[@class='text desc']/text()"
        self.phoneNumberXPath = "//div[@class='text phone']/text()"
        self.employeeSizeXPath = "//div[contains(span, 'Employees')]/text()"
        self.industryXPath = "//div[@class='categories']/a//@title"
        self.foundedOnXPath = "//div[contains(span, 'year')]/text()"
        self.companyWebXPath = "//div[@class='text weblinks']//@href"
        self.contactPersonXPath = "//div[@class='info']/div[@class='text']/text()"
        self.companyManagerXPath = "//div[contains(span, 'manager')]/text()"
        self.contactInfoXPath = "//i[@class='fa fa-check']"

    def parse(self, response):
        links = response.xpath(self.allCategoriesUrlXPath)
        for link in links:
            url = response.urljoin(link.extract())
            yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):
        links = response.xpath(self.allCompaniesUrlXPath)
        for link in links:
            url = response.urljoin(link.extract())
            yield scrapy.Request(url, callback=self.parse_main_item)
	
        nextPageUrl = response.xpath(self.nextPageUrlXPath)
        if nextPageUrl is not None:
            url = response.urljoin(nextPageUrl.extract_first())
            yield scrapy.Request(url, callback=self.parse_item)

    def parse_main_item(self, response):
        CompanyName = response.xpath(self.companyNameXPath).extract_first()

        CompanyPhoto = response.xpath(self.companyPhotoXPath).extract()
        CompanyPhoto = [os.path.basename(photo) for photo in CompanyPhoto]
        
        CompanyStreet = response.xpath(self.companyStreetXPath).extract_first()
        if CompanyStreet and CompanyStreet[-2:] == ', ' : CompanyStreet = CompanyStreet[:-2]

        CompanyCity = response.xpath(self.companyCityXPath).extract_first()

        CompanyState = response.xpath(self.companyStateXPath).extract_first()

        CompanyDesc = response.xpath(self.companyDescXPath).extract_first()
        CompanyDesc = re.sub(" +|\n|\r|\t|\0|\x0b|\xa0",' ',CompanyDesc).strip()
        CompanyDesc = re.sub("( +|\n|\r|\t|\0|\x0b|\xa0|\xbb|\xab)+",' ',CompanyDesc).strip()

        PhoneNumber = response.xpath(self.phoneNumberXPath).extract()

        EmployeeSize = response.xpath(self.employeeSizeXPath).extract_first()
        if EmployeeSize: EmployeeSize = EmployeeSize[1:]

        Industry = response.xpath(self.industryXPath).extract()
        Industry = sorted([item[:-10] for item in Industry])

        FoundedOn = response.xpath(self.foundedOnXPath).extract_first()
        if FoundedOn: FoundedOn = FoundedOn[1:]

        CompanyWeb = response.xpath(self.companyWebXPath).extract_first()

        ContactPerson = response.xpath(self.contactPersonXPath).extract()
        ContactPerson = [cp for cp in ContactPerson if cp!='Not provided']

        CompanyManager = response.xpath(self.companyManagerXPath).extract_first()
        if CompanyManager: CompanyManager = CompanyManager[1:]

        ContactInfo = response.xpath(self.contactInfoXPath).extract()
        ContactInfo = "Verified" if bool(ContactInfo) else "Unverified"

        item = ProfileItem()
        item['CreatedOn'] = self.start_time
        item['CompanyName'] = CompanyName
        item['CompanyUrl'] = response.url
        item['CompanyPhoto'] = CompanyPhoto
        item['CompanyStreet'] = CompanyStreet
        item['CompanyCity'] = CompanyCity
        item['CompanyState'] = CompanyState
        item['Country'] = 'Philippines'
        item['CompanyDesc'] = CompanyDesc
        item['PhoneNumber'] = PhoneNumber
        item['EmployeeSize'] = EmployeeSize
        item['Industry'] = Industry
        item['FoundedOn'] = FoundedOn
        item['CompanyWeb'] = CompanyWeb
        item['ContactPerson'] = ContactPerson
        item['CompanyManager'] = CompanyManager
        item['ContactInfo'] = ContactInfo
        yield item

        
