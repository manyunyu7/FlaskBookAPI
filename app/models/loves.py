import pymysql.cursors, os
from app.config import getConnection

def loves(type, type_id, user_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO loves(type, type_id, user_id) VALUES(%s,%s,%s)',
                (type, type_id, user_id))
    conn.commit()
    results = cursor.lastrowid
    conn.close()
    return results