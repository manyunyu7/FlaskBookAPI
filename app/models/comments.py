import pymysql.cursors, os
from app.config import getConnection

def comment(type, type_id, user_id, comment, createdby, isactive):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO comments(type, type_id, user_id, comment, createdby, isactive) VALUES(%s,%s,%s,%s,%s,%s)',
                (type, type_id, user_id, comment, createdby, isactive))
    conn.commit()
    results = cursor.lastrowid
    conn.close()
    return results
