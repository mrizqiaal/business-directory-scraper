from scrapy import cmdline

cmdline.execute("scrapy crawl spiderBot -o company_profiles.json -t json".split())
