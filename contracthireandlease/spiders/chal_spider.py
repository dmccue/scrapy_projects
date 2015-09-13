import scrapy

import os, json

from contracthireandlease.items import ContracthireandleaseItem

class ContractHireAndLeaseSpider(scrapy.Spider):
    name = "contracthireandlease"
    allowed_domains = ["contracthireandleasing.com"]
    start_urls = ["http://www.contracthireandleasing.com/personal/car-contract-hire-and-leasing/"]

    def parse(self, response):
        for manu in response.xpath('//*[@id="manList"]/option/@value').extract():
            url = response.urljoin(manu)
            yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):
        #Next page handling
        next_page = response.xpath('//a[@class="older-posts"]/@href')
        if next_page:
            url = "/".join(response.url.split('/')[:3] + next_page.extract())
            yield scrapy.Request(url, callback=self.parse_item)

        #Current page handling
        for car in response.xpath('//div[@id="alldeals"]/div'):
            sel = scrapy.Selector(text=car.extract(), type="html")
            item = ContracthireandleaseItem()
            link_url_string = sel.xpath('//a/@href').extract()[0]
            link_url = link_url_string.split('/')

            item['_id'] = int(link_url[::-1][1])
            item['i_model'] = link_url[::-1][2]
            item['i_manufacturer'] = link_url[::-1][3]

            item['i_desc'] = sel.xpath('//h3[@class="deal-model"]/span/text()').extract() + sel.xpath('//p[@class="deal-model-desc"]/text()').extract()

            contract_profile = sel.xpath('//p[@class="deal-profile"]/text()').extract()[0].split(' ')
            item['i_contract_mileage'] = int(contract_profile[1].replace('k','').replace('Unlimited','-1'))

            contract_months = contract_profile[0].split('+')
            item['i_contract_term'] = int(contract_months[1])

            item['i_contract_monthlyprice'] = float("".join([
                sel.xpath('//p[@class="deal-price"]/text()').extract()[0],
                sel.xpath('//p[@class="deal-price"]/span/text()').extract()[0]
            ]).replace(',','').encode('ascii','ignore'))

            item['i_contract_initial'] = float(sel.xpath('//p[@class="deal-user"]/text()').extract()[0].split(' ')[0].replace(',','').encode('ascii','ignore'))
            item['i_url'] = link_url_string
            yield item



    # def parse_item(self, response):
    #     #next handling
    #     url = 'http://www.contracthireandleasing.com' + response.xpath('//a[@class="older-posts"]/@href').extract()[0]
    #     yield scrapy.Request(url, callback=self.parse_item)
    #
    #     #item handling
    #     for car_url in response.xpath('//*[@id="alldeals"]/div/div/a/@href').extract():
    #         yield scrapy.Request(car_url, callback=self.parse_car)

    # def parse_car(self, response):
    #     item = ContracthireandleaseItem()
    #     item['i_id'] = response.url.split('/')[::-1][1]
    #     item['i_manufacturer'] = response.xpath('//span[@itemprop="brand"]/text()').extract()[0]
    #     item['i_model'] = response.xpath('//span[@itemprop="name"]/text()').extract()[0]
    #     item['i_desc'] = response.xpath('//*[@itemprop="description"]/text()').extract()[0]
    #     item['i_contract_mileage'] = response.xpath('//*[@id="hidMileageDeal"]/@value').extract()[0].replace(',','')
    #     item['i_contract_term'] = response.xpath('//*[@id="hidTermDeal"]/@value').extract()[0]
    #     item['i_contract_initial'] = response.xpath('//*[@id="hidDepositDeal"]/@value').extract()[0].replace(',','')[1:]
    #     item['i_contract_monthlyprice'] = response.xpath('//title/text()').extract()[0].split('|')[1].split(' ')[1].encode('ascii','ignore')
    #     item['i_url'] = response.url
    #
    #     json_data = {}
    #     for keyname in item.keys():
    #       json_data[keyname] = item[keyname]
    #
    #     if not os.path.exists('tmp/' + item['i_manufacturer']):  os.makedirs('tmp/' + item['i_manufacturer'])
    #     if not os.path.exists('tmp/' + item['i_manufacturer'] + '/' + item['i_model']):  os.makedirs('tmp/' + item['i_manufacturer'] + '/' + item['i_model'])
    #     if not os.path.exists('tmp/' + item['i_manufacturer'] + '/' + item['i_model'] + '/' + item['i_id']):
    #         with open('tmp/' + item['i_manufacturer'] + '/' + item['i_model'] + '/' + item['i_id'], 'w') as outfile:
    #             json.dump(json_data, outfile)
    #
    #     yield item
