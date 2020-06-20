from config.env_config import app, db, manager
import requests, os, time, hashlib, json, re
from lxml import etree
from models.movie import Movie
from config.DataHelper import getCurrentTime
import uuid

'''
Run with   python manager.py runjob -m movie 
'''


class JobTask():
    def __init__(self):
        self.source = "btbtdy"
        self.url = {
            "num": 3,
            "url": "http://kan.sogou.com/dianying/-meiguo---/",
            "path": "/tmp/%s/"
        }

    def run(self, params):
        self.parse_movie()

    def parse_movie(self):
        config = self.url
        htmlContent = self.getHtmlContent(config['url'])

        selector = etree.HTML(htmlContent)
        divs = selector.xpath("/html/body/div[5]/div/div[2]/div[1]/ul/li/*[contains(@class, 'cell ')]")
        for item in divs:
            movie_info = {}
            movie_info["name"] = item.xpath("./div/*[contains(@class, 'tit')]/a/text()")[0]
            movie_info["desc"] = item.xpath("./div/p[2]/text()")[0]
            movie_info["classify"] = ",".join(item.xpath("./div/dl[1]/dd/a/text()"))

            movie_info["director"] = "暂无"
            if item.xpath("./div/dl[2]/dd/a/text()"):
                movie_info["director"] = item.xpath("./div/dl[2]/dd/a/text()")[0]

            movie_info["actor"] = item.xpath("./div/dl[3]/dd/a/text()")[0]
            movie_info["cover_pic"] = item.xpath("./a/img/@src")[0]
            movie_info["rating"] = item.xpath("./div/dl[4]/dd/span/text()")[0]
            movie_info["is_recommend"] = 1
            movie_info["id"] = str(uuid.uuid1()).replace('-', '')
            movie_info["pub_date"] = 1
            movie_info["magnet_url"] = "1"
            movie_info["pics"] = "1"
            movie_info["online__url"] = "1"
            movie_info["visits"] = "1"
            movie_info["update_at"] = movie_info['create_at'] = getCurrentTime()

            tmp_model_movie = Movie(**movie_info)
            db.session.add(tmp_model_movie)
            db.session.commit()

    def getHtmlContent(self, url):
        """
        获取html内容
        :param url: html地址
        :return: html
        """
        try:
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.content
        except Exception:
            return None


if __name__ == "__main__":
    job = JobTask()
    job.parse_movie()

