# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import urllib
from tistory.items import TistoryItem


class TistoryCrawler(scrapy.Spider):
    name = 'tistory'
    def __init__(self, url, folder):
        self.start_urls = [url]
        self.folder = folder
    def parse(self, response):
        res = BeautifulSoup(response.body)
        for img in res.select('img'):
            url = img['src']
            if (url[0] == 'h'):
                url = url.replace("image", "original")
                yield scrapy.Request(url, self.parse_details)

    def parse_details(self, response):
        str = response.headers['Content-Disposition'].decode('utf-8').split('"')
        target = 'filename'
        i = 0
        for s in str:
            i += 1
            if s.find(target) > 0:
                break;

        name = str[i]
        print(self.folder.encode('utf-8'))
        tistoryitem = TistoryItem()
        tistoryitem['image_urls'] = [response.url]
        tistoryitem['name'] = name
        tistoryitem['path'] = 'D:\I.O.I\\' + self.folder + '\\'
        return tistoryitem





