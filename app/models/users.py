import pymysql.cursors, os
from app.config import getConnection

def getuser(user_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * from view_users WHERE user_id = %s ''',
        (user_id))
    results = cursor.fetchall()
    conn.close()
    return results

def getuserbyemail(email):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * from view_users WHERE email = %s ''',
        (email))
    results = cursor.fetchall()
    conn.close()
    return results

def fetchbysignin(username, email, password):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT  u.user_id, u.username, ur.role_id, u.email, u.firstname, u.middlename, u.lastname
        FROM users u 
            join user_role ur 
                ON u.user_id = ur.user_id 
        WHERE u.password = %s 
            AND ur.role_id = 2 
            AND u.isactive = 1 
            AND ( username LIKE %s 
                    OR email LIKE %s )''',
        (password, username, email))
    results = cursor.fetchall()
    conn.close()
    return results

def authorgenre(user_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT
            name
        FROM
            (
            SELECT
                g.name,
                COUNT( * ) AS JML,
                u.user_id
            FROM
                books_rel_author bra
                JOIN users u ON bra.author_id = u.user_id
                JOIN books_rel_genres brg ON bra.book_id = brg.book_id
                JOIN genres g ON brg.genre_id = g.id 
            WHERE
                u.user_id = %s 
            GROUP BY
                g.NAME 
            ) genres_author 
        ORDER BY
            JML DESC 
            LIMIT 3''',
        (user_id))
    results = cursor.fetchall()
    conn.close()
    return results

def authorjobdesc(user_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT name 
        FROM
            (
            SELECT
                cp.name,
                count( * ) AS JML,
                bra.author_id 
            FROM
                books_rel_author bra
                JOIN creator_profession cp ON bra.label = cp.id 
            WHERE
                bra.author_id = %s 
            GROUP BY
                cp.name 
            ) jobdesc_author 
        ORDER BY
            JML DESC 
            LIMIT 2''',
        (user_id))
    results = cursor.fetchall()
    conn.close()
    return results

def fetchAllAuthorFollowed(user_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT u.user_id AS user_id, 
            u.username   AS username, 
            u.firstname  AS firstname, 
            u.middlename AS middlename, 
            u.lastname   AS lastname, 
            u.picture    AS picture, 
            ufa.created  AS created_at 
        FROM user_follow_author ufa 
            join users u 
                ON ufa.author_id = u.user_id 
            join user_author ua 
                ON u.user_id = ua.user_id 
        WHERE  ufa.user_id = %s 
            AND ua.user_id IS NOT NULL 
        ORDER  BY ufa.created DESC ''',
        (user_id))
    results = cursor.fetchall()
    conn.close()
    return results

def authorrellabel(table, i, name):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *, CONCAT(u.firstname, ' ', u.middlename, ' ', u.lastname) as fullname, cp.name label_info
        FROM 
            '''+table+''' bu, users u, creator_profession cp 
        WHERE 
            bu.'''+name+''' = u.user_id 
            AND bu.label = cp.id 
            AND bu.book_id = %s''',
        (i))
    results = cursor.fetchall()
    conn.close()
    return results

def authorrellabelbyid(i, book_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *, CONCAT(u.firstname, ' ', u.middlename, ' ', u.lastname) as fullname, cp.name label_info
        FROM 
            books_rel_author bu, users u, creator_profession cp 
        WHERE 
            bu.author_id = u.user_id 
            AND bu.label = cp.id 
            AND bu.book_id = %s
			AND cp.id = %s''',
        (book_id, i))
    results = cursor.fetchall()
    conn.close()
    return results    
    
def fetchallauthor():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *,
            CONCAT(u.firstname, ' ', u.middlename, ' ', u.lastname) as fullname,
            ua.created as created_at,
            ua.createdby as created_by
        FROM user_author ua 
            join users u 
                ON ua.user_id = u.user_id 
        ORDER BY ua.created desc''')
    results = cursor.fetchall()
    conn.close()
    return results  

def reviwersbyuser(user_id, data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *,
            b.title as booktitle,
            CONCAT(u.firstname,' ',u.middlename,' ',u.lastname) as fullname,
            br.created as createdreview,
            br.createdby as createdbyreview,
            br.title as titlereview,
			(select love_id from loves l where l.user_id = '''+user_id+''' and l.type = 'books_review' and l.type_id = br.book_review_id) as isloved,
			(select COUNT(love_id) from loves where type = 'books_review' and type_id = br.book_review_id) as totallove,
			(select COUNT(comment_id) from comments where type = 'books_review' and type_id = br.book_review_id) as totalcomment
        FROM books_review br 
            join books b
                ON br.book_id = b.book_id
            join users u 
                ON br.user_id = u.user_id 
        WHERE '''+data)
    results = cursor.fetchall()
    conn.close()
    return results 

def labels(): 
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT id, name 
        FROM creator_profession 
        WHERE isactive=1''')
    results = cursor.fetchall()
    conn.close()
    return results 

def totalreader(reader, authorid): 
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT count(*) as totalreader
        FROM books_rel_status_user bs 
        WHERE bs.reading_status_id='''+reader+''' AND bs.user_id='''+authorid)
    results = cursor.fetchone()
    conn.close()
    return results 

def usersosmedbyid(user_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT sm.sosmed_id,
            sm.name,
            sm.code,
            sm.url,
            us.sosmedname,
            us.user_id
        FROM user_sosmed us
            JOIN social_media sm
                ON sm.sosmed_id = us.sosmed_id 
        WHERE user_id='''+user_id)
    results = cursor.fetchall()
    conn.close()
    return results 

def following(id, data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT u.*,
            CONCAT(u.firstname,' ',u.middlename,' ',u.lastname) as fullname,
		    (select count(fd.friend_id) from friends fd where (fd.user_id = uf.author_id or fd.user_friend_id = uf.author_id) and fd.isaccepted = 1 and fd.isblock != 1) as TotalFriends,
		    (select getTotalMutualFriends('''+id+''',uf.author_id)) as TotalMutualFriends
        FROM user_follow_author uf
            JOIN users u
                ON uf.author_id = u.user_id 
        WHERE '''+data)
    results = cursor.fetchall()
    conn.close()
    return results 

def fetchpeoplefollowdiscuss(discuss_id, myid):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT u.*,
        CONCAT(u.firstname,' ',u.middlename,' ',u.lastname) as fullname,
		(select count(fd.friend_id) from friends fd where (fd.user_id = bfd.user_id or fd.user_friend_id = bfd.user_id) and fd.isaccepted = 1 and fd.isblock != 1) as TotalFriends,
		(select getTotalMutualFriends('''+myid+''',bfd.user_id)) as TotalMutualFriends
        FROM books_follow_discussion bfd
            JOIN users u
                ON bfd.user_id = u.user_id 
        WHERE bfd.book_discuss_id='''+discuss_id)
    results = cursor.fetchall()
    conn.close()
    return results 

def followers(id, data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT u.*,
            CONCAT(u.firstname,' ',u.middlename,' ',u.lastname) as fullname,
            (select count(fd.friend_id) from friends fd where (fd.user_id = uf.user_id or fd.user_friend_id = uf.user_id) and fd.isaccepted = 1 and fd.isblock != 1) as TotalFriends,
            (select getTotalMutualFriends('''+id+''',uf.user_id)) as TotalMutualFriends
        FROM user_follow_author uf
            JOIN users u
                ON uf.user_id = u.user_id 
        WHERE '''+data)
    results = cursor.fetchall()
    conn.close()
    return results 

def user(firstname, middlename, lastname, username, password, email, biodata, birthdate, place_birthdate, gender, country, city, province, phone, isactive, picture, createdby, editedby):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users(firstname, middlename, lastname, username, password, email, biodata, birthdate, place_birthdate, gender, country, city, province, phone, isactive, picture, createdby, editedby) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                (firstname, middlename, lastname, username, password, email, biodata, birthdate, place_birthdate, gender, country, city, province, phone, isactive, picture, createdby, editedby))
    conn.commit()
    results = True
    conn.close()
    return results

def userreqbook(user_id, book_id, status, createdby):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user_req_books(user_id, book_id, status, createdby) VALUES(%s,%s,%s,%s)',
                (user_id, book_id, status, createdby))
    conn.commit()
    results = cursor.lastrowid
    conn.close()
    return results

def creatorprofession(name, isactive):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO creator_profession(name, isactive) VALUES(%s,%s)',
                (name, isactive))
    conn.commit()
    results = cursor.lastrowid
    conn.close()
    return results

def register(firstname, middlename, lastname, username, password, email, isactive, url_slug, createdby):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users(firstname, middlename, lastname, username, password, email, isactive, url_slug, createdby) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                (firstname, middlename, lastname, username, password, email, isactive, url_slug, createdby))
    conn.commit()
    results = cursor.lastrowid
    conn.close()
    return results

def userrole(user_id, role_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user_role(user_id, role_id) VALUES(%s,%s)',
                (user_id, role_id))
    conn.commit()
    results = "success"
    conn.close()
    return results

def userauthor(user_id, isapproved, createdby):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user_author(user_id, isapproved, createdby) VALUES(%s,%s,%s)',
                (user_id, isapproved, createdby))
    conn.commit()
    results = cursor.lastrowid
    conn.close()
    return results

def userfollowauthor(user_id, author_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user_follow_author(user_id, author_id) VALUES(%s,%s)',
                (user_id, author_id))
    conn.commit()
    results = True
    conn.close()
    return results

def notif(user_id, for_user_id, category, message, link):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO notifications(user_id, for_user_id, category, message, link) VALUES(%s,%s,%s,%s,%s)',
                (user_id, for_user_id, category, message, link))
    conn.commit()
    results = cursor.lastrowid
    conn.close()
    return results

def updatenotif(for_user_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE notifications SET isread = 1 WHERE for_user_id = %s',
                (for_user_id))
    conn.commit()
    results = True
    conn.close()
    return results

def userauthorrelposition(books_rel_author_id, position_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user_author_rel_position(books_rel_author_id, position_id) VALUES(%s,%s)',
                (books_rel_author_id, position_id))
    conn.commit()
    results = cursor.lastrowid
    conn.close()
    return results

def usersosmed(user_id, sosmed_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user_sosmed(user_id, sosmed_id) VALUES(%s,%s)',
                (user_id, sosmed_id))
    conn.commit()
    results = True
    conn.close()
    return results

def usergenre(user_id, genre_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user_genre(user_id, genre_id) VALUES(%s,%s)',
                (user_id, genre_id))
    conn.commit()
    results = True
    conn.close()
    return results

def lastlogon(lastlogon,user_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE users set lastlogon=%s WHERE user_id=%s',
                (lastlogon, user_id))
    conn.commit()
    results = True
    conn.close()
    return results

def systempass(password, user_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE users set password=%s WHERE user_id=%s',
                (password, user_id))
    conn.commit()
    results = "Berhasil"
    conn.close()
    return results

def isactive(isactv, user_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE users set isactive=%s WHERE user_id=%s',
                (isactv, user_id))
    conn.commit()
    results = True
    conn.close()
    return results

def updateuser(firstname, middlename, lastname, email, biodata, birthdate, place_birthdate, gender, country, city, province, phone, picture, editedby, user_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE users set firstname=%s, middlename=%s, lastname=%s, email=%s, biodata=%s, birthdate=%s, place_birthdate=%s, gender=%s, country=%s, city=%s, province=%s, phone=%s, picture=%s, editedby=%s WHERE user_id=%s',
                (firstname, middlename, lastname, email, biodata, birthdate, place_birthdate, gender, country, city, province, phone, picture, editedby, user_id))
    conn.commit()
    results = True
    conn.close()
    return results

def updateuserpic(picture, user_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE users set picture=%s WHERE user_id=%s',
                (picture, user_id))
    conn.commit()
    results = True
    conn.close()
    return results

def updateuseradm(firstname, middlename, lastname, username, email, biodata, birthdate, place_birthdate, gender, country, city, province, phone, picture, editedby, url_slug, user_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE users set firstname=%s, middlename=%s, lastname=%s, username=%s, email=%s, biodata=%s, birthdate=%s, place_birthdate=%s, gender=%s, country=%s, city=%s, province=%s, phone=%s, picture=%s, editedby=%s, url_slug=%s WHERE user_id=%s',
                (firstname, middlename, lastname, username, email, biodata, birthdate, place_birthdate, gender, country, city, province, phone, picture, editedby, url_slug, user_id))
    conn.commit()
    results = True
    conn.close()
    return results

def userscountersearch(user_id, count):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users_counter_search(user_id, count) VALUES(%s,%s)',
                (user_id, count))
    conn.commit()
    results = True
    conn.close()
    return results

def updateuserscountersearch(user_id, count, id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE users_counter_search SET user_id=%s, count=%s WHERE user_counter_search_id=%s ',
                (user_id, count, id))
    conn.commit()
    results = True
    conn.close()
    return results

def fetchonecreator():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT  ua.* ,(SELECT
                        `cp`.`name`
                    FROM
                        (
                            `books_rel_author` `ba`
                        JOIN `creator_profession` `cp`
                        ON
                            (`cp`.`id` = `ba`.`label`)
                        )
                    WHERE
                        `ba`.`author_id` = `ua`.`user_id`
                    LIMIT 1) as label 
        FROM view_author ua
        WHERE isactive=1 AND TotalFollowers is not null
        ORDER BY RAND()
        LIMIT 1''')
    results = cursor.fetchall()
    conn.close()
    return results

def fetchsixcreator(id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT  *
        FROM view_author
        WHERE isactive=1 AND TotalFollowers is not null AND user_id != %s
        ORDER BY RAND()''',(id))
    results = cursor.fetchall()
    conn.close()
    return results