import json
import pymssql

with open('./Movies.json', 'r', encoding='utf-8') as f:
    rows_str = f.read()

config = {
    'server':"127.0.0.1",
    'user':"zhanglin",
    'password':"jeroami233",
    'database':"SpiderData",
    'port': '1433'
}

db = pymssql.connect(**config)


Movies = json.loads(rows_str)
cur = db.cursor()
    
for Movie in Movies:
    insert = f"INSERT INTO Movies VALUES(N\"{Movie['title']}\", N\"{Movie['oth_title']}\", N\"{Movie['category']}\", {Movie['rating_num']})".replace('\'', '\'\'').replace('\"', '\'')
    print([insert])
    cur.execute(insert)
        
db.commit()
cur.close()
db.close()