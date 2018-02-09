# encoding: utf-8
import requests
from bs4 import BeautifulSoup
import time
from pymongo import MongoClient

"""
2018年01月11日21:28:57
in Xueyuan road, BJ
"""


def get_article_url(article):
    """
    返回文章链接
    :param article: 文本内容对象
    :return: artical csdn url
    """
    article_url = article.select('div.list_ad > span > a')
    if article_url:
        return article_url[0]['href']


def get_article_title(article):
    title = article.select('dd.tracking-ad > span > a.title')
    if title:
        return title[0].text


def get_publish_time_and_read_num(article):

    res = article.select('dd.tracking-ad > ul.list-inline > li')
    read_num = article.select('li > em')
    result = []
    if res and len(res) > 1:
        result.append(res[1].text)
    else:
        result.append(None)

    if read_num:
        result.append(read_num[0].text)
    else:
        result.append(None)
    return result


def from_article_get_info(article):
    article_url = get_article_url(article)
    title = get_article_title(article)
    pb_and_rn = get_publish_time_and_read_num(article)
    return title, article_url, pb_and_rn[0], pb_and_rn[1]


def get_final_article_id(page_articles):
    """
    返回下一页请求所需id
    :param page_articles: 当页文章内容
    :return: 下一页请求所需id
    """
    final_article_info = from_article_get_info(page_articles[-1])
    final_article_id = final_article_info[1].split('/')[-1]
    return final_article_id


def store(data):
    insert_data = {'title': data[0],
                   'article_url': data[1],
                   'publish_time': data[2],
                   'read_num': data[3]}
    article_table.insert(insert_data)


def one_page(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'lxml')
    articles = soup.select('dl.geek_list')
    for article in articles:
        article_info = from_article_get_info(article)
        store(article_info)
    return get_final_article_id(articles)


def connect_mongo(uri):
    conn = MongoClient(uri)
    return conn


def jktt_crawler():
    next_page_id = one_page('http://geek.csdn.net/forum/AI')
    for page in range(1, 50):
        next_page_id = one_page(url.format(page, next_page_id))
        time.sleep(6)


url = 'http://geek.csdn.net/forum/43?t=&page={}&last_id=6%3A{}'
mongo_conn = connect_mongo('mongodb://localhost:27017/jktt')
article_table = mongo_conn.jktt.article
jktt_crawler()

"""
需求较为简单，且为demo项目，故使用requests+BeautifulSoup完成
生产需求下的项目，个人一般使用scrapy

数据库类型：mongodb
数据库名称：jktt， 表名: article
数据库结构：
title: 文章名称
article_url: 文章链接
publish_time: 发布时间
read_num: 阅读数


上述代码已实现 
爬虫程序爬取该页面下最新发布的 1000 篇文章信息，并且将数据存入数据库

实现每天增量爬取更新的文章：(仅提出方案，emm..而且实现技术也不难，明天还得上班..你懂的:) 偏向第二种策略)
    
    观察网页中数据发现，最热 栏目下的数据并非按照时间排序
    故不能使用时间顺序来判断是否爬取过
    
    假设 爬虫每日启动一次，爬取完今日内容则停止。
    策略一：
        当日，记录 启动后爬取到的首篇文章的id，并存入数据库
        爬虫正常运行...
        次日，读取上述id记录，当再次遇到此id时，停止爬取
        
    策略一缺点：
        当首篇文章的id 意外重复时，会导致错误的停止
        
    策略二：
        每次爬取时，将爬取过的id存入redis数据库。当访问新数据时，
        连续重复特定数量后（例如 50条数据相同时），停止爬取
        
        redis定时清理
    策略二缺点：
        存储代价增加，需要额外查询

        
    策略三：（仅针对使用scrapy的情况）
        在scrapy中增加spider middleware,将每个item计算fingerprint存入set做去重
        当此fingerprint已存在，则不把item提交到spider进行处理，需要的话同时记录重复数量
        当重复数量到达一定阈值，暂停爬虫
        
        明日恢复爬虫的运行
    策略三优点：
        减少重复item的处理，提高效率，减少重复存储
    策略三缺点:
        消耗内存
        
暂且只想到三种，如有更好设计，欢迎交流，echooc@outlook.com
"""
