import pymysql.cursors, os
from app.config import getConnection

def review(book_id, user_id, title, rate, review, createdby):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books_review(book_id, user_id, title, rate, review, createdby) VALUES(%s,%s,%s,%s,%s,%s)',
                (book_id, user_id, title, rate, review, createdby))
    conn.commit()
    results = cursor.lastrowid
    conn.close()
    return results

def updatereview(title, rate, review, id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE books_review SET title=%s, rate=%s, review=%s WHERE book_review_id=%s',
                (title, rate, review, id))
    conn.commit()
    results = True
    conn.close()
    return results

def ratereview(book_id, user_id, rate):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE books_review SET rate=%s WHERE book_id=%s AND user_id=%s',
                (rate, book_id, user_id))
    conn.commit()
    results = True
    conn.close()
    return results