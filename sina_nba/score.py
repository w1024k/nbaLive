# coding: utf-8

import requests, sys
from lxml import etree
import settings
import time


class Score(object):
    def __init__(self, url=None):
        self.url = url or settings.SCORE_URL

    def get_node(self):
        params = {
            "vt": 4,
            "livetype": "nba",
        }
        index_text = requests.get(url=self.url, params=params, headers=settings.HEADERS).text
        selector = etree.HTML(index_text)
        node = selector.xpath('//dl')
        return node

    def get_score(self):

        node = self.get_node()
        score_list = list()

        for node1 in node:
            score = node1.xpath('.//h2[@class ="live_h2"]/a/text()')[0]
            score_list.append(score)

        return ' '.join(score_list).encode('utf-8')

    def get_rooms(self):
        node = self.get_node()
        live_id_list = list()
        live_desc = list()

        for node1 in node:
            score = node1.xpath('.//h2[@class ="live_h2"]/a/text()')[0]
            links = node1.xpath(".//h4/a/@href")[0]

            live_id = links.split("=")[-1]
            live_id_list.append(live_id)
            live_desc.append(score)

        return live_id_list, live_desc

    def run(self, start=True):
        if start:
            rate = 0
        else:
            rate = raw_input("刷新频率(秒,0为不刷新):")
            try:
                rate = int(rate)
            except:
                rate = 0

        if rate == 0:
            detail = self.get_score()
            print detail
        else:
            while True:
                detail = self.get_score()
                sys.stdout.write(detail + "\r")
                time.sleep(rate)
                sys.stdout.flush()


if __name__ == '__main__':
    a = Score()
    print a.get_rooms()
