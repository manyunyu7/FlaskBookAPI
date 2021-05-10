import pymysql.cursors, os
from app.config import getConnection

def feed(user_id, feeds, isactivity, ispublic, createdby, type, typeData):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO feeds(user_id, feeds, isactivity, ispublic, createdby, type, typeData) VALUES(%s,%s,%s,%s,%s,%s,%s)',
                (user_id, feeds, isactivity, ispublic, createdby, type, typeData))
    conn.commit()
    results = cursor.lastrowid
    conn.close()
    return results

def mentionfeed(feed_id, datatype, dataid):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO mention_feeds(feed_id, datatype, dataid) VALUES(%s,%s,%s)',
                (feed_id, datatype, dataid))
    conn.commit()
    results = True
    conn.close()
    return results