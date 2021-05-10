import pymysql.cursors, os
from app.config import getConnection


def byid(table, data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *
        FROM '''+table+''' 
        WHERE '''+data)
    results = cursor.fetchone()
    conn.close()
    return results

def tableviewrow(table, data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *
        FROM '''+table+''' 
        WHERE '''+data)
    results = cursor.fetchone()
    conn.close()
    return results

def tableviewresult(table, data, orderby):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *
        FROM '''+table+''' 
        WHERE '''+data+'''
        ORDER BY '''+orderby)
    results = cursor.fetchall()
    conn.close()
    return results

def fetchalldata(table):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *
        FROM '''+table)
    results = cursor.fetchall()
    conn.close()
    return results

def fetchdataall(table, data, orderby):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *
        FROM '''+table+''' 
        WHERE '''+data+'''
        ORDER BY '''+orderby)
    results = cursor.fetchall()
    conn.close()
    return results

def fetchcodition(table, data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *
        FROM '''+table+''' 
        WHERE '''+data)
    results = cursor.fetchall()
    conn.close()
    return results

def fetchconditionhighlight(table, data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *, CONCAT('http://komiqus-dev-9-api.kilatiron.com/assets/img/books/uploads/',REPLACE(cover,'.//assets//img//books//uploads//','')) covermobile
        FROM '''+table+''' 
        WHERE '''+data)
    results = cursor.fetchall()
    conn.close()
    return results

def fetchorderby(table, orderby):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *
        FROM '''+table+''' 
        ORDER BY '''+orderby)
    results = cursor.fetchall()
    conn.close()
    return results

def callstoredprocedure(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def fetchallmenu():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *,
            (case when isactive = 1 then 'Active' else 'Non Active' end )as isactive_label,
            (case when isBackend = 1 then 'Backend' else 'Frontend' end ) as isbackend_label,
            (case when isMain = 1 then 'Main menu' else 'Child' end ) as isMain_label
        FROM menu
        ORDER BY code asc ''')
    results = cursor.fetchall()
    conn.close()
    return results

def fetchmymessagelist(id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT * 
        FROM message m 
			JOIN message_content mc
                ON mc.message_id = m.message_id 
                and mc.created = (select max(created) from message_content where message_id = m.message_id 
                and created <= m.updated)
		WHERE (m.user_one = '''+id+''' or m.user_two = '''+id+''') 
        ORDER BY m.updated desc ''')
    results = cursor.fetchall()
    conn.close()
    return results

def fetchmynotif(data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *, 
            no.created as notifdate, 
            CONCAT(u.firstname,' ',u.middlename,' ',u.lastname) as fullname
        FROM notifications no
			JOIN users u
                ON no.user_id = u.user_id
		WHERE '''+data+''' 
        ORDER BY no.created DESC''')
    results = cursor.fetchall()
    conn.close()
    return results

def fetchmynotiflimit(data, rowperpage, row):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *, 
            no.created as notifdate, 
            CONCAT(u.firstname,' ',u.middlename,' ',u.lastname) as fullname
        FROM notifications no
			JOIN users u
                ON no.user_id = u.user_id
		WHERE '''+data+''' 
        ORDER BY no.created DESC
        LIMIT '''+rowperpage+''' OFFSET '''+row)
    results = cursor.fetchall()
    conn.close()
    return results

def fetchcontentbymenu(data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *
        FROM content_tbl c
			JOIN section_book s
                ON s.section_id = c.section_id
		WHERE '''+data+''' 
        ORDER BY c.order_position ASC''')
    results = cursor.fetchall()
    conn.close()
    return results

def fetchsidebartbl(data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT c.sidebar_id,
            c.belongsto,
            c.order_position,
            c.ispath,
            c.name as pathname,
            c.path,
            c.layout, 
            c.isactive as sidebar_active, 
            s.*,
            (case when ((s.type = 'AG' and s.algo_name = 'TA') or (s.type = 'AG' and s.algo_name = 'AA') or (s.type = 'RCA') ) then 'Author' else 'Book' end) as layout_tipe_dsc,
			m.name as menu_name,(select l.`name` from label_type l where l.`code` = c.layout) as layout_name,
			(select l.name from label_type l where l.`code` = s.type) as content_type,
			(select l.name from label_type l where l.`code` = s.algo_name) as content_type_algo
        FROM sidebar_tbl c
			JOIN section_book s
                ON s.section_id = c.section_id
            JOIN menu m
                ON m.code = c.belongsto
		WHERE '''+data+''' 
        ORDER BY c.order_position ASC''')
    results = cursor.fetchall()
    conn.close()
    return results

def insert(table, column, data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO '+table+'('+column+') VALUES('+(data)+')')
    conn.commit()
    results = cursor.lastrowid
    conn.close()
    return results

def delete(table, data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM '+table+' WHERE '+data)
    conn.commit()
    results = True
    conn.close()
    return results

def fetchroleadm():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT role_id
        FROM user_role 
        WHERE role_id !=2 
        ORDER BY role_id ASC''')
    results = cursor.fetchall()
    conn.close()
    return results

def fetchroleadmuserbyid(user_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT role_id
        FROM user_role 
        WHERE role_id !=2 and user_id = %s
        ORDER BY role_id ASC''',(user_id))
    results = cursor.fetchall()
    conn.close()
    return results