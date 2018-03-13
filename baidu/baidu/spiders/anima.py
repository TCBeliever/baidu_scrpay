# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
from scrapy.loader import ItemLoader, Identity
from baidu.items import BaiduItem
import json
from pprint import pprint
from time import sleep
import logging


keyword = ""
tag = ""
rn = 50
loop = 40
BASE_URL = '''https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%s&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%s&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&cg=girl&pn=%d&rn=%d&gsm=1e&1506655596737='''

def _gen_next_url():
    fix = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    global keyword, tag
    fin = open('anima.txt')
    for line in fin.readlines():
        array = line.split(' ')[0].split(':')
        keyword, tag = array[0], array[1]
        for i in range(len(fix)):
            query = keyword + fix[i]
            for j in range(loop):
                url = BASE_URL %(query, query, (j*rn), rn)
                yield url

class ImageSpider(scrapy.Spider):
    global tag
    name = 'baidu_anima'
    allowed_domains = ['bdstatic.com', 'baidu.com']
    #first_page = _gen_next_url()
    start_urls = (_gen_next_url())
    logging.info("start urls: {}".format(start_urls))

    #a generator for broswer pages
    def parse(self, response):
        jsonresp = json.loads(response.body_as_unicode())
        for o in jsonresp['data']:
            if 'thumbURL' in o:
                l = ItemLoader(item=BaiduItem(), response=response)
                #image_url
                l.add_value('image_urls', o['thumbURL'])
                l.add_value('image_type', tag)
                yield l.load_item()

