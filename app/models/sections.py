import pymysql.cursors, os
from app.config import getConnection

def fetchcontenttbl(data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT c.*,
            s.`name`,
            s.description,
            s.isactive as section_active,
            s.type,
            s.algo_name, 
            s.note,
            s.created,
            s.createdby,
            s.edited,
            s.editedby,
            (case when ((s.type = 'AG' and s.algo_name = 'TA') or (s.type = 'AG' and s.algo_name = 'AA') or (s.type = 'RCA') ) then 'Author' else 'Book' end) as layout_tipe_dsc,
            m.`name` as menu_name,(select l.`name` from label_type l where l.`code` = c.layout) as layout_name,
            (select l.name from label_type l where l.`code` = s.type) as content_type,
            (select l.name from label_type l where l.`code` = s.algo_name) as content_type_algo
        FROM content_tbl c
            JOIN section_book s
                ON s.section_id = c.section_id
            JOIN menu m
                ON m.code = c.belongsto
        WHERE '''+data+'''
        ORDER BY menu_name, c.order_position ASC''')
    results = cursor.fetchall()
    conn.close()
    return results

def sectionbook(name, description, type, algo_name, isactive, createdby):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO section_book(name, description, type, algo_name, isactive, createdby) VALUES(%s,%s,%s,%s,%s,%s)',
                (name, description, type, algo_name, isactive, createdby))
    conn.commit()
    results = cursor.lastrowid
    conn.close()
    return results

def updatesectionbook(name, description, type, algo_name, isactive, createdby, section_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE section_book SET name=%s, description=%s, type=%s, algo_name=%s, isactive=%s, createdby=%s WHERE section_id=%s',
                (name, description, type, algo_name, isactive, createdby, section_id))
    conn.commit()
    results = True
    conn.close()
    return results

def sectionbooklist(section_id, book_id, addedby):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO section_book_list(section_id, book_id, addedby) VALUES(%s,%s,%s)',
                (section_id, book_id, addedby))
    conn.commit()
    results = True
    conn.close()
    return results

def sectionbookcontent(name, description, type, algo_name, editedby, section_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE section_book SET name=%s, description=%s, type=%s, algo_name=%s, editedby=%s WHERE section_id=%s',
                (name, description, type, algo_name, editedby, section_id))
    conn.commit()
    results = True
    conn.close()
    return results

def sidebar(belongsto, order_position, section_id, isactive, layout):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO sidebar_tbl(belongsto, order_position, section_id, isactive, layout) VALUES(%s,%s,%s,%s,%s)',
                (belongsto, order_position, section_id, isactive, layout))
    conn.commit()
    results = cursor.lastrowid
    conn.close()
    return results

def updatesidebar(belongsto, isactive, layout, section_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE sidebar_tbl SET belongsto=%s, isactive=%s, layout=%s WHERE sidebar_id=%s',
                (belongsto, isactive, layout, section_id))
    conn.commit()
    results = True
    conn.close()
    return results

def positionsidebar(order_position, sidebar_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE sidebar_tbl SET order_position=%s WHERE sidebar_id=%s',
                (order_position, sidebar_id))
    conn.commit()
    results = True
    conn.close()
    return results

def contenttbl(isactive, layout, belongsto, content_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE content_tbl SET isactive=%s, layout=%s, belongsto=%s WHERE content_id=%s',
                (isactive, layout, belongsto, content_id))
    conn.commit()
    results = True
    conn.close()
    return results

def positioncontent(order_position, content_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE content_tbl SET order_position=%s WHERE content_id=%s',
                (order_position, content_id))
    conn.commit()
    results = True
    conn.close()
    return results