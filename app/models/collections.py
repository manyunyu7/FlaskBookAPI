import pymysql.cursors, os
from app.config import getConnection

def collection(name, user_id, description, isactive, ispublic, createdby):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO collection_user(name, user_id, description, isactive, ispublic, createdby) VALUES(%s,%s,%s,%s,%s,%s)',
                (name, user_id, description, isactive, ispublic, createdby))
    conn.commit()
    results = cursor.lastrowid
    conn.close()
    return results

def updatecollection(name, user_id, description, isactive, ispublic, createdby, collection_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE collection_user SET name=%s, user_id=%s, description=%s, isactive=%s, ispublic=%s, createdby=%s WHERE collection_id='+collection_id,
                (name, user_id, description, isactive, ispublic, createdby))
    conn.commit()
    results = True
    conn.close()
    return results

def updatefavoritecollection(isfavorite, order_position_fav, collection_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE collection_user SET isfavorite=%s, order_position_fav=%s WHERE collection_id='+collection_id,
                (isfavorite, order_position_fav))
    conn.commit()
    results = True
    conn.close()
    return results