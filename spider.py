
import pymysql
import pymssql
import requests
from lxml import etree
import time
import sys,re,json


#爬虫系统 

config = {
    'server':"127.0.0.1",
    'user':"zhanglin",
    'password':"jeroami233",
    'database':"SpiderData",
    'port': '1433'
}

current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
    # 'content-type': 'text/html;charset=utf-8',
    }


def MovieSpider(page, db):
    print(f'Reading Page{page}...', end='')
    url = f'http://movie.douban.com/top250?start={page * 25}'
    
    req = requests.get(url, headers=headers, timeout=10)
    response = req.content.decode('utf-8')
    selector = etree.HTML(response)

    
    def get_movie_list(): # 获取电影名称[(中文名[, 外文名, ...,]), (中文名[, 外文名, ...,]), ...]
        movie_list = selector.xpath('//div[@class="info"]/div[@class="hd"]/a')
        movie_title_item_list = [tuple(i.xpath('span[@class="title"]/text()')) for i in movie_list]
        title_list = [tuple([n.encode().decode('utf-8') for n in i]) for i in movie_title_item_list]
        # result
        title_list = [tuple(n.replace(u'\xa0', '').replace('/', '') for n in i) for i in title_list]
        return title_list
    
    
    def get_movie_desc(): # 获取电影分类/描述
        movie_description_p = selector.xpath('//div[@class="info"]/div[@class="bd"]/p')
        description_item_list = [tuple([i.encode('utf-8').decode('utf-8').replace('\n', '').strip() for i in p.xpath('text()')]) for p in movie_description_p]
        # result
        description_item_list = [tuple(s.replace(u'\xa0', '') for s in item) for item in description_item_list if any(item)]
        desc_list = [i[1].split('/')[-1] for i in description_item_list]
        return desc_list
    
    def get_rating_num(): # 获取电影评分
        movie_rating_span = selector.xpath('//div[@class="info"]//span[@class="rating_num"]/text()')
        rating_list = [float(i.encode().decode('utf-8')) for i in movie_rating_span]
        return rating_list
    
    def get_picture_link():
        img_list = selector.xpath('//div[@class="item"]//img/@src')
        img_list = [i.encode().decode('utf-8') for i in img_list]
        return img_list
        
    Movies = []
    row = zip(get_movie_list(), get_movie_desc(), get_rating_num(), get_picture_link())
    for i in row:
        Movie = {}
        Movie['title'] = i[0][0]
        Movie['oth_title'] = i[0][1] if len(i[0]) > 1 else ''
        Movie['category'] = i[1]
        Movie['rating_num'] = i[2]
        Movie['picture'] = i[3]
        Movies.append(Movie)
    time.sleep(0.5)
    
    # desc_list = get_movie_desc()
    # print(json.dumps(desc_list, indent=2, ensure_ascii=False))
    # print(len(desc_list))
    
    
    # 数据库
    cur = db.cursor()
    for Movie in Movies:
        insert = f"INSERT INTO polls_movie (title, oth_title, category, rating_num, picture) VALUES(N\"{Movie['title']}\", N\"{Movie['oth_title']}\", N\"{Movie['category']}\", {Movie['rating_num']}, \"{Movie['picture']}\")"\
                 .replace('\'', '\'\'')\
                 .replace('\"', '\'')
        print(insert)
        cur.execute(insert)
    db.commit()
    cur.close()
   


if __name__ == '__main__':
    print('Begin')
    db = pymssql.connect(**config)
    cur = db.cursor()
    # cur.execute('delete from polls_movie')
    db.commit()
    for p in range(0,10):
        MovieSpider(p, db)
    db.close()