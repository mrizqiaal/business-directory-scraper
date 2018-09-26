# Business Directory Scraper
Crawls company profile information from a comprehensive business directory of companies in Philippines (<a href="https://www.businesslist.ph">PhilippinesBusinessList</a>) using **Scrapy** and store them into **MongoDB**.

## Environment
Works on Ubuntu 16.04 LTS

Language: Python 3.5.2

Database: MongoDB

Depedencies:
* <a href="https://doc.scrapy.org/en/latest/intro/install.html">Scrapy</a>
* <a href="http://api.mongodb.com/python/current/installation.html">Pymongo</a>

## Instructions for use
### Pre-boot configuration
* Install MongoDB and start without configuration (create database and collection)

* Install Python dependent modules： Scrapy, pymongo, requests or

        $ pip install -r requirements.txt

### Start up

    $ cd PhilippinesBusinessList
    $ python3 quickstart.py

## Run screenshot
<img src="https://github.com/mrizqiaal/business-directory-scraper/blob/master/studio3t.png?raw=true" width = "800" height = "400" align=center />   
