# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv

import pymysql
from scrapy.utils.project import get_project_settings


class MaoyanPipeline:
    def __init__(self):
        settings = get_project_settings()
        self.connect = pymysql.connect(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            port=settings['MYSQL_PORT'],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True
        )

    def process_item(self, item, spider):
        self.cursor = self.connect.cursor()
        sql = "INSERT INTO maoyan(name, tag, time) VALUES(%s, %s, %s)"
        params = (item["name"], item["tag"], item["time"])
        self.cursor.execute(sql, params)
        self.connect.commit()
        self.cursor.close()

    def close_spider(self, spider):
        self.connect.close()




