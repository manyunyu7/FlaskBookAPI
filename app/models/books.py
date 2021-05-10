import pymysql.cursors, os
from app.config import getConnection

def authorbooks(table, i, name):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *
        FROM '''+table+''' bu 
            join books b 
                ON bu.'''+name+''' = b.book_id 
        WHERE bu.author_id = %s
            AND b.isactive = 1
        GROUP BY bu.'''+name,
        (i))
    results = cursor.fetchall()
    conn.close()
    return results

def authorbookscode(table, i, name, code):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT b.*, 
               s.name statusbook, 
               t.name typebook, 
               (SELECT sum(brlu.rate)/5 FROM books_rel_rate_user brlu WHERE brlu.book_id = b.book_id ) AS TotalRating
        FROM '''+table+''' bu 
            join books b 
                ON bu.'''+name+''' = b.book_id
            join status s
                ON b.status = s.id
            join types t
                ON b.type = t.id
        WHERE bu.author_id = %s
            AND b.isactive = 1
            AND b.code != '''+code+'''
        GROUP BY bu.'''+name,
        (i))
    results = cursor.fetchall()
    conn.close()
    return results

def authorinbook(book_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *,
            u.user_id ,CONCAT(u.firstname,' ',u.middlename,' ',u.lastname) as fullname,
            cp.name label_info,
            cp.id as id_label 
        FROM books_rel_author bu, users u, creator_profession cp 
        WHERE bu.author_id=u.user_id AND bu.label = cp.id AND bu.book_id ='''+book_id)
    results = cursor.fetchall()
    conn.close()
    return results

def bookbycode(code):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *,
            (case when (b.status = 1) then 'New' 
			  when (b.status = 2) then 'updated' 
			  when (b.status = 3) then 'on going' 
			  when (b.status = 4) then 'completed' 
		 	  else 'None' end ) as statusbook,
	 	  	(case when (b.type = 1) then 'Printing' 
			  when (b.type = 2) then 'digital' 
			  when (b.type = 3) then 'web comic'  
		 	  else 'None' end ) as typebook, 
	 	  	(select sum(rate)/5 from books_rel_rate_user where book_id = b.book_id) as rating,
            DATE_FORMAT(release_date, '%d %m %Y') as published
        FROM books b
        WHERE code='''+code)
    results = cursor.fetchone()
    conn.close()
    return results

def bookbymyreq(book_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *,
            urb.created as createdreq,
            urb.createdby as createdbyreq,
            urb.edited as editedreq,
            urb.editedby as editedbyreq, 
            (case when (urb.status = 1) then 'Approved by Admin' 
                when (urb.status = 2) then 'Rejected by Admin' 
            else 'Need approved by Admin' end ) as statusreq  
        FROM user_req_books urb
        WHERE book_id='''+book_id)
    results = cursor.fetchone()
    conn.close()
    return results

def bookbygenre(id_genre):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *
        FROM books_rel_genres
        WHERE genre_id IN ('''+id_genre+''')
        GROUP BY book_id''')
    results = cursor.fetchall()
    conn.close()
    return results

def fetchbookgenre(genre_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT * 
        FROM books b JOIN books_rel_genres brg ON (b.book_id=brg.book_id) 
        WHERE brg.genre_id = %s AND b.isactive = 1''',(genre_id))
    results = cursor.fetchall()
    conn.close()
    return results

    
def fetchbookgenremobile(genre_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *, CONCAT('http://komiqus-dev-9-api.kilatiron.com/assets/img/books/uploads/',REPLACE(cover,'.//assets//img//books//uploads//','')) covermobile
        FROM books b JOIN books_rel_genres brg ON (b.book_id=brg.book_id) 
        WHERE brg.genre_id = %s AND b.isactive = 1''',(genre_id))
    results = cursor.fetchall()
    conn.close()
    return results

def bookbystatus(data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *
        FROM books_rel_status_user bu
            JOIN books b
                ON b.book_id = bu.book_id
        WHERE '''+data)
    results = cursor.fetchall()
    conn.close()
    return results

def bookforseries(data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *
        FROM books_rel_series brs
            JOIN books b
                ON b.book_id = brs.book_id
            JOIN status s
                ON s.id = b.status
        WHERE '''+data)
    results = cursor.fetchall()
    conn.close()
    return results


def bookforcollection(data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *,
            c.created as createdCollection, 
            c.createdby as createdCollectionBy, 
            (select sum(rate)/5 from books_rel_rate_user where book_id = b.book_id) as rating,
            s.name as statusname
        FROM books_rel_collection c
            JOIN books b
                ON b.book_id = c.book_id
            JOIN status s
                ON s.id = b.status
        WHERE '''+data+'''
        ORDER BY c.created DESC''')
    results = cursor.fetchall()
    conn.close()
    return results

def bookreluser(table, i, name):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *, CONCAT(u.firstname,' ',u.middlename,' ',u.lastname) as fullname
        FROM '''+table+''' bu 
            join users u 
                ON bu.'''+name+''' = u.user_id 
        WHERE bu.book_id = %s
        GROUP BY bu.'''+name,
        (i))
    results = cursor.fetchall()
    conn.close()
    return results

def bookreluserwatcher(id, table, i, name):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *, 
            CONCAT(u.firstname,' ',u.middlename,' ',u.lastname) as fullname,
            (select getTotalMutualFriends('''+id+''',u.user_id)) as TotalMutualFriends
        FROM '''+table+''' bu 
            join users u 
                ON bu.'''+name+''' = u.user_id 
        WHERE bu.book_id = %s
        GROUP BY bu.'''+name,
        (i))
    results = cursor.fetchall()
    conn.close()
    return results

def bookreluserseries(series_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT DISTINCT CONCAT(u.firstname,' ',u.middlename,' ',u.lastname) as fullname, 
            username as username
        FROM books_rel_author bu
            JOIN users u
                ON bu.author_id = u.user_id
            JOIN books b
                ON b.book_id = bu.book_id
            JOIN books_rel_series brs
                ON b.book_id = brs.book_id
        WHERE brs.book_seriesid='''+series_id)
    results = cursor.fetchall()
    conn.close()
    return results

def bookrelgenre(table, i):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *
        FROM '''+table+''' bu 
            join genres g 
                ON bu.genre_id = g.id 
        WHERE bu.book_id = %s''',
        (i))
    results = cursor.fetchall()
    conn.close()
    return results

def booklabel(book_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT DISTINCT
        bra.label, cp.name as label_info
    FROM
        books_rel_author bra JOIN creator_profession cp ON bra.label = cp.id
    WHERE
        book_id =  %s''',
        (book_id))
    results = cursor.fetchall()
    conn.close()
    return results


def genresbook(book_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *,
            (select bg.book_id from books_rel_genres bg where bg.genre_id = g.id and bg.book_id = '''+book_id+''') as ishad
        FROM genres g 
        ORDER BY g.name ASC''')
    results = cursor.fetchall()
    conn.close()
    return results

def feedrow(data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *
        FROM mention_feeds a
            join feeds b
                ON b.feed_id = a.feed_id 
        WHERE '''+data)
    results = cursor.fetchone()
    conn.close()
    return results

def fetchallrequest():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *,
        urb.created as createdreq,
        urb.createdby as createdbyreq,
        urb.edited as editedreq,
        urb.editedby as editedbyreq, 
		(case when (urb.status = 1) then 'Approved' 
			  when (urb.status = 2) then 'Rejected' 
		else 'Pendings' end ) as statusreq,
        CONCAT(u.firstname,' ',u.middlename,' ',u.lastname) as fullname
        FROM user_req_books urb
            join users u
                ON urb.user_id = u.user_id
            join books b
                ON b.book_id = urb.book_id
        ORDER BY urb.created DESC''')
    results = cursor.fetchall()
    conn.close()
    return results

def fetchallmyrequest(id_user):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *,
        urb.created as createdreq,
        urb.createdby as createdbyreq,
        urb.edited as editedreq,
        urb.editedby as editedbyreq, 
		(case when (urb.status = 1) then 'Approved' 
			  when (urb.status = 2) then 'Rejected' 
		else 'Pendings' end ) as statusreq,
        CONCAT(u.firstname,' ',u.middlename,' ',u.lastname) as fullname
        FROM user_req_books urb
            join users u
                ON urb.user_id = u.user_id
            join books b
                ON b.book_id = urb.book_id
        WHERE urb.user_id='''+id_user+'''
        ORDER BY urb.created DESC''')
    results = cursor.fetchall()
    conn.close()
    return results

def fetchbookhasstatus(book_id, id_user):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *,
            (select book_rel_status_user_id from books_rel_status_user where book_id = '''+book_id+'''
            and rs.id = reading_status_id and user_id = '''+id_user+''') as hasbookid
        FROM reading_status rs''')
    results = cursor.fetchall()
    conn.close()
    return results



def fetchallmyseries(data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT DISTINCT bs.book_seriesid,
            s.name
        FROM books_series s
            JOIN books_rel_series bs
                ON s.book_seriesid = bs.book_seriesid
            JOIN books b
                ON bs.book_id = b.book_id
            JOIN books_rel_author ba
                ON b.book_id = ba.book_id
            JOIN users u
                ON ba.author_id = u.user_id
        WHERE '''+data)
    results = cursor.fetchall()
    conn.close()
    return results

def fetchdiscuss(id_user, data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *,
            CONCAT(u.firstname,' ',u.middlename,' ',u.lastname) as fullname, 
            bd.created as createddiscuss, 
            bd.createdby as createdbydiscuss, 
            bd.title as titlediscuss, 
            (select book_follow_discuss_id from books_follow_discussion bfd where bfd.user_id = '''+id_user+''' and bfd.book_discuss_id = bd.book_discuss_id) as isfollow,
			(select love_id from loves l where l.user_id = '''+id_user+''' and l.type = 'books_discussion' and l.type_id = bd.book_discuss_id) as isloved,
			(select COUNT(love_id) from loves where type = 'books_discussion' and type_id = bd.book_discuss_id) as totallove,
			(select COUNT(comment_id) from comments where type = 'books_discussion' and type_id = bd.book_discuss_id) as totalcomment
        FROM books_discussion bd
            JOIN users u
                ON bd.user_id = u.user_id
            JOIN books b
                ON bd.book_id = b.book_id
        WHERE '''+data)
    results = cursor.fetchone()
    conn.close()
    return results

def fetchallactvdiscuss(id_user):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *,
            CONCAT(u.firstname,' ',u.middlename,' ',u.lastname) as fullname, 
            bd.created as createddiscuss, 
            bd.createdby as createdbydiscuss, 
            bd.title as titlediscuss, 
            (select book_follow_discuss_id from books_follow_discussion bfd where bfd.user_id = '''+id_user+''' and bfd.book_discuss_id = bd.book_discuss_id) as isfollow,
			(select love_id from loves l where l.user_id = '''+id_user+''' and l.type = 'books_discussion' and l.type_id = bd.book_discuss_id) as isloved,
			(select COUNT(love_id) from loves where type = 'books_discussion' and type_id = bd.book_discuss_id) as totallove,
			(select COUNT(comment_id) from comments where type = 'books_discussion' and type_id = bd.book_discuss_id) as totalcomment
        FROM books_discussion bd
            JOIN users u
                ON bd.user_id = u.user_id
            JOIN books b
                ON bd.book_id = b.book_id
        WHERE bd.isactive=1''')
    results = cursor.fetchall()
    conn.close()
    return results 

def fetchallactvdiscussbyauthor(author_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *,
            CONCAT(u.firstname,' ',u.middlename,' ',u.lastname) as fullname, 
            bd.created as createddiscuss, 
            bd.createdby as createdbydiscuss
        FROM books_discussion bd
            JOIN books_rel_author ba
                ON ba.book_id = bd.book_id
            JOIN users u
                ON bd.user_id = u.user_id
        WHERE bd.isactive=1 AND ba.author_id='''+author_id)
    results = cursor.fetchall()
    conn.close()
    return results

def fetchallactvdiscussbybook(book_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *,
            CONCAT(u.firstname,' ',u.middlename,' ',u.lastname) as fullname, 
            bd.created as createddiscuss, 
            bd.createdby as createdbydiscuss,
            post as post
        FROM books_discussion bd
            JOIN users u
                ON bd.user_id = u.user_id
        WHERE bd.isactive=1 AND bd.book_id='''+book_id)
    results = cursor.fetchall()
    conn.close()
    return results 

def fetchallactvdiscussbybookfollow(book_id, id_user):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *,
            CONCAT(u.firstname,' ',u.middlename,' ',u.lastname) as fullname, 
            bd.created as createddiscuss, 
            bd.createdby as createdbydiscuss
        FROM books_discussion bd
            JOIN users u
                ON bd.user_id = u.user_id
            JOIN books_follow_discussion d
                ON bd.book_discuss_id = d.book_discuss_id
        WHERE bd.isactive=1 AND bd.book_id='''+book_id+''' AND d.user_id='''+id_user )
    results = cursor.fetchall()
    conn.close()
    return results 

def fetchallactvreviewbybook(book_id, id_user):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *,
            CONCAT(u.firstname,' ',u.middlename,' ',u.lastname) as fullname, 
            br.created as createdreview, 
            br.createdby as createdbyreview, 
            (select love_id from loves l where l.user_id = '''+id_user+''' and l.type = 'books_review' and l.type_id = br.book_review_id) as isloved,
			(select COUNT(love_id) from loves where type = 'books_review' and type_id = br.book_review_id) as totallove,
			(select COUNT(comment_id) from comments where type = 'books_review' and type_id = br.book_review_id) as totalcomment
        FROM books_review br
            JOIN users u
                ON br.user_id = u.user_id
        WHERE br.isblock=0 AND br.book_id='''+book_id)
    results = cursor.fetchall()
    conn.close()
    return results

def fetchallmydicuss(id_user):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *,
            CONCAT(u.firstname,' ',u.middlename,' ',u.lastname) as fullname, 
            bd.created as createddiscuss, 
            bd.createdby as createdbydiscuss, 
            b.title as booktitle, 
            bd.title as titlediscuss,
			(select love_id from loves l where l.user_id = '''+id_user+''' and l.type = 'books_discussion' and l.type_id = bd.book_discuss_id) as isloved, 
            (select COUNT(love_id) from loves where type = 'books_discussion' and type_id = bd.book_discuss_id) as totallove
        FROM books_discussion bd
            JOIN users u
                ON bd.user_id = u.user_id
            JOIN books b
                ON bd.book_id = b.book_id
            JOIN books_follow_discussion d
                ON bd.book_discuss_id = d.book_discuss_id
        WHERE bd.isactive=1 AND d.user_id='''+id_user+'''
        GROUP BY bd.book_id''')
    results = cursor.fetchall()
    conn.close()
    return results 

def fetchallcomment(data, id_user):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *,
            CONCAT(u.firstname,' ',u.middlename,' ',u.lastname) as fullname, 
            c.created as created_comment, 
            c.createdby as createdby_comment, 
            c.edited as edited_comment, 
            c.editedby as editedby_comment, 
			(select l.love_id from loves l where l.type='comments' and l.type_id= c.comment_id and l.user_id = '''+id_user+''') as loved_id,
			(select COUNT(love_id) from loves where type = 'comments' and type_id = c.comment_id) as totallove,
			(select COUNT(comment_id) from comments where type = 'comments' and type_id = c.comment_id) as totalcomment
        FROM comments c
            JOIN users u
                ON u.user_id = c.user_id
        WHERE '''+data+'''
        ORDER BY c.created''')
    results = cursor.fetchall()
    conn.close()
    return results

def fetchbyrole(data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT m.*
        FROM access_menu am
            JOIN menu m
                ON m.menu_id = am.menu_id
        WHERE '''+data+'''
        ORDER BY m.urutan ASC''')
    results = cursor.fetchall()
    conn.close()
    return results

def fetchcollectiondropdown(book_id, id_user):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT cu.*, 
            (select bc.book_rel_collection_id from books_rel_collection bc WHERE bc.book_id = '''+book_id+''' 
            and bc.collection_id = cu.collection_id) as hasbookcollectionid
        FROM collection_user cu
        WHERE cu.user_id='''+id_user+''' AND cu.isactive=1''')
    results = cursor.fetchall()
    conn.close()
    return results

def fetchallmyactvcollection(data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *
        FROM collection_user c
            JOIN users u
                ON c.user_id=u.user_id
        WHERE '''+data+'''
        ORDER BY c.order_collection ASC''')
    results = cursor.fetchall()
    conn.close()
    return results

def fetchallinmonth():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *, 
            (TotalViewerMonth + TotalReviewMonth + TotalDiscussMonth) as TotalScore
        FROM view_top_book_month
        WHERE (TotalViewerMonth + TotalReviewMonth + TotalDiscussMonth) <> 0
        ORDER BY TotalScore DESC''')
    results = cursor.fetchall()
    conn.close()
    return results

def rate(data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT count(rate) as numberofrate
        FROM books_rel_rate_user
        WHERE '''+data)
    results = cursor.fetchone()
    conn.close()
    return results

def rateseries(series_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT ROUND(SUM(IFNULL((SELECT sum(br.rate)/count(br.book_id) from books_rel_rate_user br WHERE br.book_id = brs.book_id),0))/count(brs.book_seriesid),1) as rate from books_rel_series brs where brs.book_seriesid ='''+series_id)
    results = cursor.fetchall()
    conn.close()
    return results

def relbook(table, data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *
        FROM '''+table+''' bu 
            join books b
                ON bu.book_id = b.book_id
            join genres g 
                ON bu.genre_id = g.id 
        WHERE '''+data)
    results = cursor.fetchall()
    conn.close()
    return results

def relatecollectionbybook(data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *
        FROM books_rel_collection bc
            JOIN collection_user cu
                ON cu.collection_id = bc.collection_id
            JOIN users a
                ON a.user_id = cu.user_id
        WHERE '''+data+'''
        ORDER BY cu.collection_id ASC''')
    results = cursor.fetchall()
    conn.close()
    return results

def search(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *
        FROM view_books_and_users
        WHERE lower(name) LIKE %s and role='users'
        ORDER BY count DESC
        LIMIT 5''',(query))
    results = cursor.fetchall()
    conn.close()
    return results

def searchmobile(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *
        FROM view_books
        WHERE lower(title) LIKE %s and isactive = 1
        ORDER BY title''',(query))
    results = cursor.fetchall()
    conn.close()
    return results

def searchbook(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *
        FROM view_books_and_users
        WHERE lower(name) LIKE %s and role='books'
        ORDER BY count DESC
        LIMIT 5''',(query))
    results = cursor.fetchall()
    conn.close()
    return results

def searchseries(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT book_seriesid as id, name  as series, status as status
        FROM books_series
        WHERE lower(name) LIKE %s ''',(query))
    results = cursor.fetchall()
    conn.close()
    return results

def seriesbyid(i):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT bs.book_seriesid, bs.name, bs.status
        FROM books_rel_series brs
            JOIN books_series bs
                ON brs.book_seriesid = bs.book_seriesid
        WHERE brs.book_id = %s''',
        (i))
    results = cursor.fetchone()
    conn.close()
    return results

def statusbookseries(data):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT (select s.name from status s where s.id=bs.status) as status, 
            count(b.volume) as volume, 
            SUM(b.chapter) as chapter
        FROM books_rel_series brs
            JOIN books b
                ON b.book_id = brs.book_id
            JOIN books_series bs
                ON brs.book_seriesid = bs.book_seriesid
        WHERE '''+data)
    results = cursor.fetchall()
    conn.close()
    return results

def trandingweek():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *, (TotalViewerWeek + TotalReviewWeek + TotalDiscussWeek) as TotalScore
        FROM view_top_book_week
        WHERE (TotalViewerWeek + TotalReviewWeek + TotalDiscussWeek) <> 0
        ORDER BY TotalScore DESC
        LIMIT 6''')
    results = cursor.fetchall()
    conn.close()
    return results

def newrelease():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *
        FROM view_books
        WHERE isactive = 1
        ORDER BY release_date DESC
        LIMIT 12''')
    results = cursor.fetchall()
    conn.close()
    return results

def newreleasemobile():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT *, CONCAT('http://komiqus-dev-9-api.kilatiron.com/assets/img/books/uploads/',REPLACE(cover,'.//assets//img//books//uploads//','')) covermobile
        FROM view_books
        WHERE isactive = 1
        ORDER BY release_date DESC
        LIMIT 12''')
    results = cursor.fetchall()
    conn.close()
    return results

def lastaddbook(id_user):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT cu.collection_id,
            cu.user_id,
            ( CONCAT('KMQSBKCLL000',cu.collection_id) ) as collection_code,
            cu.`name` as collection_name,cu.description as collection_desc,
			cu.ispublic,cu.isactive,
            cu.number_of_order,
            cu.created as collection_added, 
            cu.edited as collection_edited, 
            b.*
        FROM books_rel_collection bc
            JOIN collection_user cu
                ON bc.collection_id = cu.collection_id
            JOIN books b
                ON b.book_id = bc.book_id
        WHERE cu.user_id = '''+id_user+'''
        GROUP BY cu.collection_id
        ORDER BY bc.created DESC''')
    results = cursor.fetchone()
    conn.close()
    return results

def book(code, title, alternate, release_date,  type, synopsis, chapter, volume, page, rank, language, isbn, issn, status, type_publisher, publisher, createdby, isactive, cover, preview):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books(code, title, alternate, release_date,  type, synopsis, chapter, volume, page, rank, language, isbn, issn, status, type_publisher, publisher, createdby, isactive, cover, preview) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                (code, title, alternate, release_date,  type, synopsis, chapter, volume, page, rank, language, isbn, issn, status, type_publisher, publisher, createdby, isactive, cover, preview))
    conn.commit()
    results = cursor.lastrowid
    conn.close()
    return results

def bookrelauthor(book_id, author_id, label):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books_rel_author(book_id, author_id, label) VALUES(%s,%s,%s)',
                (book_id, author_id, label))
    conn.commit()
    results = cursor.lastrowid
    conn.close()
    return results

def insertbookrelgenre(book_id, genre_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books_rel_genres(book_id, genre_id) VALUES(%s,%s)',
                (book_id, genre_id))
    conn.commit()
    results = True
    conn.close()
    return results

def bookrellink(book_id, link, categories):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books_rel_link(book_id, link, categories) VALUES(%s,%s,%s)',
                (book_id, link, categories))
    conn.commit()
    results = True
    conn.close()
    return results

def bookseries(name, isactive, createdby):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books_series(name, isactive, createdby) VALUES(%s,%s,%s)',
                (name, isactive, createdby))
    conn.commit()
    results = cursor.lastrowid
    conn.close()
    return results

def bookrelseries(book_id, book_seriesid):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books_rel_series(book_id, book_seriesid) VALUES(%s,%s)',
                (book_id, book_seriesid))
    conn.commit()
    results = True
    conn.close()
    return results

def bookcounterview(book_id, user_id, count):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books_counter_view(book_id, user_id, count) VALUES(%s,%s,%s)',
                (book_id, user_id, count))
    conn.commit()
    results = True
    conn.close()
    return results

def bookscountersearch(book_id, count):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books_counter_search(book_id, count) VALUES(%s,%s)',
                (book_id, count))
    conn.commit()
    results = True
    conn.close()
    return results

def bookrelstatususer(book_id, reading_status_id, user_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books_rel_status_user(book_id, reading_status_id, user_id) VALUES(%s,%s,%s)',
                (book_id, reading_status_id, user_id))
    conn.commit()
    results = True
    conn.close()
    return results

def updatebookrelstatususer(book_id, reading_status_id, user_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE books_rel_status_user SET reading_status_id=%s WHERE book_id=%s AND user_id=%s',
                (reading_status_id, book_id, user_id))
    conn.commit()
    results = True
    conn.close()
    return results

def updatediscuss(title, isquestion, topic, book_discuss_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE books_discussion SET title=%s, isquestion=%s, topic=%s WHERE book_discuss_id=%s ',
                (title, isquestion, topic, book_discuss_id))
    conn.commit()
    results = True
    conn.close()
    return results

def updatepostdiscuss(created, post, book_discuss_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE books_discussion SET created=%s, post=%s WHERE book_discuss_id=%s ',
                (created, post, book_discuss_id))
    conn.commit()
    results = True
    conn.close()
    return results

def updatebookcounterview(book_id, user_id, count, id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE books_counter_view SET book_id=%s, user_id=%s, count=%s WHERE book_counter_view_id=%s ',
                (book_id, user_id, count, id))
    conn.commit()
    results = True
    conn.close()
    return results

def updatebookscountersearch(book_id, count, id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE books_counter_search SET book_id=%s, count=%s WHERE book_counter_search_id=%s ',
                (book_id, count, id))
    conn.commit()
    results = True
    conn.close()
    return results

def booksrelrateuser(book_id, rate, user_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books_rel_rate_user(book_id, rate, user_id) VALUES(%s,%s,%s)',
                (book_id, rate, user_id))
    conn.commit()
    results = True
    conn.close()
    return results

def bookrelcollection(book_id, collection_id, createdby):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books_rel_collection(book_id, collection_id, createdby) VALUES(%s,%s,%s)',
                (book_id, collection_id, createdby))
    conn.commit()
    results = True
    conn.close()
    return results

def discuss(book_id, user_id, title, isquestion, topic, createdby, isactive):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books_discussion(book_id, user_id, title, isquestion, topic, createdby, isactive) VALUES(%s,%s,%s,%s,%s,%s,%s)',
                (book_id, user_id, title, isquestion, topic, createdby, isactive))
    conn.commit()
    results = cursor.lastrowid
    conn.close()
    return results

def deletediscuss(book_discuss_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books_discussion WHERE book_discuss_id = %s', (book_discuss_id))
    conn.commit()
    results = True
    conn.close()
    return results
    

def booksfollowdiscuss(user_id, book_discuss_id, createdby):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books_follow_discussion(user_id, book_discuss_id, createdby) VALUES(%s,%s,%s)',
                (user_id, book_discuss_id, createdby))
    conn.commit()
    results = cursor.lastrowid
    conn.close()
    return results

def updatebooksrelrateuser(book_id, rate, user_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE books_rel_rate_user SET rate=%s WHERE book_id=%s AND user_id=%s',
                (rate, book_id, user_id))
    conn.commit()
    results = True
    conn.close()
    return results

def updatebookseries(book_seriesid, status_id):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('UPDATE books_series SET status=%s WHERE book_seriesid=%s',
                (status_id, book_seriesid))
    conn.commit()
    results = True
    conn.close()
    return results