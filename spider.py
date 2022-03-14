
import pymysql
import requests
from lxml import etree
import time
import sys,re,json


#爬虫系统 
config = {
    'host':"127.0.0.1",
    'user':"root",
    'passwd':"wutuxing750",
    'database':"test"
}

""" db = pymysql.connect(**config) """

current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
    # 'content-type': 'text/html;charset=utf-8',
}

def getdetail(url):
    req = requests.get(url, headers=headers, timeout=10)
    response = req.content
    selector = etree.HTML(response)
    count = selector.xpath('//span[@class="addListCount"]/text()')
    detail = re.findall('"description":(.*?),"shielded"', req.text)[0][:-2]
    author = re.findall('"author":(.*?),"cover"', req.text)[0][:-2]
    return count, detail, author

def MovieSpider(page):

    url = f'https://movie.douban.com/top250?start={(page-1) * 25}'

    req = requests.get(url, headers=headers, timeout=10)
    response = req.content.decode('utf-8')
    selector = etree.HTML(response)
    # print(response)

    movie_list = selector.xpath('//div[@class="info"]/div[@class="hd"]/a')
    movie_title_item_list = [tuple(i.xpath('span[@class="title"]/text()')) for i in movie_list]
    title_list = [tuple([n.encode('utf-8').decode('utf-8') for n in i]) for i in movie_title_item_list]
    title_list = [tuple(n.replace(u'\xa0', '').replace('/', '') for n in i) for i in title_list]
    print(title_list)
    # 数据库
    """ cur = db.cursor()
    for name, link, tag,author,scorenum, bcount, detail in zip(list_name, list_book,list_tag, list_author,list_score,list_count, list_detail):
        insert = "INSERT INTO `myapp_book`(id, cate_id,name, link, tag,author,scorenum,bcount, detail,time) VALUES(NULL,NULL, '%s', '%s', '%s', '%s', '%s','%s', '%s','%s')" %(name, link, tag,author,scorenum,bcount, detail,current_time)
        cur.execute(insert)
        db.commit()
    cur.close() """


if __name__ == '__main__':
    # for p in range(1,3):
    MovieSpider(0)