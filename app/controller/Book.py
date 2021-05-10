from app.models import books, users
from app import response, app
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from flask import request


@jwt_required
def Authorbook(table, i, name):
    try :
        message = ""    
        results = books.authorbooks(table, i, name)
        if not results:
             message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Authorbookcode(table, i, name, code):
    try :
        message = ""    
        results = books.authorbookscode(table, i, name, code)
        if not results:
             message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Authorinbook(book_id):
    try :
        message = ""    
        results = books.authorinbook(book_id)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Bookreluser(table, i, name):
    try :
        message = ""    
        results = books.bookreluser(table, i, name)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Bookreluserwatcher(id, table, i, name):
    try :
        message = ""    
        results = books.bookreluserwatcher(id, table, i, name)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Bookbycode(code):
    try :
        message = ""    
        results = books.bookbycode(code)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Bookbymyreq(book_id):
    try :
        message = ""    
        results = books.bookbymyreq(book_id)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Bookbygenre(id_genre):
    try :
        message = ""    
        results = books.bookbygenre(id_genre)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Bookbystatus(data):
    try :
        message = ""    
        results = books.bookbystatus(data)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Bookforseries(data):
    try :
        message = ""    
        results = books.bookforseries(data)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Bookforcollection(data):
    try :
        message = ""    
        results = books.bookforcollection(data)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Bookreluserseries(series_id):
    try :
        message = ""    
        results = books.bookreluserseries(series_id)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Bookrelgenre(table, i):
    try :
        message = ""    
        results = books.bookrelgenre(table, i)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Booklabel(book_id):
    try :
        message = ""    
        results = books.booklabel(book_id)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)


@jwt_required
def Genresbook(book_id):
    try :
        message = ""    
        results = books.genresbook(book_id)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchallrequest():
    try :
        message = ""    
        results = books.fetchallrequest()
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchallmyrequest(id_user):
    try :
        message = ""    
        results = books.fetchallmyrequest(id_user)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchbookhasstatus(book_id, id_user):
    try :
        message = ""    
        results = books.fetchbookhasstatus(book_id, id_user)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)
    
@jwt_required
def Fetchdiscuss(id_user, data):
    try :
        message = ""    
        results = books.fetchdiscuss(id_user, data)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchallmydicuss(id_user):
    try :
        message = ""    
        results = books.fetchallmydicuss(id_user)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

    
@jwt_required
def Fetchallactvdiscuss(id_user):
    try :
        message = ""    
        results = books.fetchallactvdiscuss(id_user)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchallactvdiscussbyauthor(author_id):
    try :
        message = ""    
        results = books.fetchallactvdiscussbyauthor(author_id)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchallactvdiscussbybook(book_id):
    try :
        message = ""    
        results = books.fetchallactvdiscussbybook(book_id)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchallactvdiscussbybookfollow(book_id, id_user):
    try :
        message = ""    
        results = books.fetchallactvdiscussbybookfollow(book_id, id_user)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchallactvreviewbybook(book_id, id_user):
    try :
        message = ""    
        results = books.fetchallactvreviewbybook(book_id, id_user)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchallmyseries(data):
    try :
        message = ""    
        results = books.fetchallmyseries(data)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchallcomment(data, id_user):
    try :
        message = ""    
        results = books.fetchallcomment(data, id_user)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchcollectiondropdown(book_id, id_user):
    try :
        message = ""    
        results = books.fetchcollectiondropdown(book_id, id_user)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchallmyactvcollection(data):
    try :
        message = ""    
        results = books.fetchallmyactvcollection(data)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchallinmonth():
    try :
        message = ""    
        results = books.fetchallinmonth()
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Feedrow(data):
    try :
        message = ""    
        results = books.feedrow(data)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchbyrole(data):
    try :
        message = ""    
        results = books.fetchbyrole(data)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Rate(data):
    try :
        message = ""    
        results = books.rate(data)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Rateseries(series_id):
    try :
        message = ""    
        results = books.rateseries(series_id)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Relbook(table, data):
    try :
        message = ""    
        results = books.relbook(table, data)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Reviwersbyuser(user_id, data):
    try :
        message = ""    
        results = users.reviwersbyuser(user_id, data)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Relatecollectionbybook(data):
    try :
        message = ""    
        results = books.relatecollectionbybook(data)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Search(query):
    try :
        message = ""    
        results = books.search(query)
        if not results:
             message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Searchmobile(query):
    try :
        message = ""
        que = "%"+query+"%"    
        results = books.searchmobile(que)
        if not results:
             message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Searchbook(query):
    try :
        message = ""    
        results = books.searchbook(query)
        if not results:
             message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Searchseries(query):
    try :
        message = ""    
        results = books.searchseries(query)
        if not results:
             message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Seriesbyid(i):
    try :
        message = ""    
        results = books.seriesbyid(i)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Statusbookseries(data):
    try :
        message = ""    
        results = books.statusbookseries(data)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Trandingbooks():
    try :
        message = ""    
        results = books.trandingweek()
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)
    
@jwt_required
def Newrelease():
    try :
        message = ""    
        results = books.newrelease()
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Newreleasemobile():
    try :
        message = ""    
        results = books.newreleasemobile()
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required

def Lastaddbook(id_user):
    try :
        message = ""    
        results = books.lastaddbook(id_user)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)
# ================= INSERT DATA ======================= #
@jwt_required
def Book():
    try :
        #GET DATA  
        code = request.form.get('code')
        title = request.form.get('title')
        alternate = request.form.get('alternate')
        release_date = request.form.get('release_date')
        type = request.form.get('type')
        synopsis = request.form.get('synopsis')
        chapter = request.form.get('chapter')
        volume = request.form.get('volume')
        page = request.form.get('page')
        rank = request.form.get('rank')
        language = request.form.get('language')
        isbn = request.form.get('isbn')
        issn = request.form.get('issn')
        status = request.form.get('status')
        type_publisher = request.form.get('type_publisher')
        publisher = request.form.get('publisher')
        createdby = request.form.get('createdby')
        isactive = request.form.get('isactive')
        cover = request.form.get('cover')
        preview = request.form.get('preview')

        # Insert data 
        results = books.book(code, title, alternate, release_date,  type, synopsis, chapter, volume, page, rank, language, isbn, issn, status, type_publisher, publisher, createdby, isactive, cover, preview)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Bookrelauthor():
    try :
        #GET DATA  
        book_id = request.form.get('book_id')
        author_id = request.form.get('author_id')
        label = request.form.get('label')

        # Insert data 
        results = books.bookrelauthor(book_id, author_id, label)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Insertbookrelgenre():
    try :
        #GET DATA  
        book_id = request.form.get('book_id')
        genre_id = request.form.get('genre_id')

        # Insert data 
        results = books.insertbookrelgenre(book_id, genre_id)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Bookrellink():
    try :
        #GET DATA  
        book_id = request.form.get('book_id')
        link = request.form.get('link')
        categories = request.form.get('categories')

        # Insert data 
        results = books.bookrellink(book_id, link, categories)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Bookseries():
    try :
        #GET DATA  
        name = request.form.get('name')
        isactive = request.form.get('isactive')
        createdby = request.form.get('createdby')

        # Insert data 
        results = books.bookseries(name, isactive, createdby)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

def Updatebookseries():
    try :
        #GET DATA  
        book_seriesid = request.form.get('book_seriesid')
        status_id = request.form.get('status_id')

        # Insert data 
        results = books.updatebookseries(book_seriesid, status_id)

        #Cek data
        if not results:
            return response.badRequest([], 'update data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Bookrelseries():
    try :
        #GET DATA  
        book_id = request.form.get('book_id')
        book_seriesid = request.form.get('book_seriesid')

        # Insert data 
        results = books.bookrelseries(book_id, book_seriesid)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Bookcounterview():
    try :
        #GET DATA  
        book_id = request.form.get('book_id')
        user_id = request.form.get('user_id')
        count = request.form.get('count')

        # Insert data 
        results = books.bookcounterview(book_id, user_id, count)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

def Updatebookcounterview(id):
    try :
        #GET DATA  
        book_id = request.form.get('book_id')
        user_id = request.form.get('user_id')
        count = request.form.get('count')

        # Insert data 
        results = books.updatebookcounterview(book_id, user_id, count, id)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Bookscountersearch():
    try :
        #GET DATA  
        book_id = request.form.get('book_id')
        count = request.form.get('count')

        # Insert data 
        results = books.bookscountersearch(book_id, count)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

def Updatebookscountersearch(id):
    try :
        #GET DATA  
        book_id = request.form.get('book_id')
        count = request.form.get('count')

        # Insert data 
        results = books.updatebookscountersearch(book_id, count, id)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Bookrelstatususer():
    try :
        #GET DATA  
        book_id = request.form.get('book_id')
        reading_status_id = request.form.get('reading_status_id')
        user_id = request.form.get('user_id')

        # Insert data 
        results = books.bookrelstatususer(book_id, reading_status_id, user_id)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

def Updatebookrelstatususer():
    try :
        #GET DATA  
        book_id = request.form.get('book_id')
        reading_status_id = request.form.get('reading_status_id')
        user_id = request.form.get('user_id')

        # Insert data 
        results = books.updatebookrelstatususer(book_id, reading_status_id, user_id)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Booksrelrateuser():
    try :
        #GET DATA  
        book_id = request.form.get('book_id')
        rate = request.form.get('rate')
        user_id = request.form.get('user_id')

        # Insert data 
        results = books.booksrelrateuser(book_id, rate, user_id)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Bookrelcollection():
    try :
        #GET DATA  
        book_id = request.form.get('book_id')
        collection_id = request.form.get('collection_id')
        createdby = request.form.get('createdby')

        # Insert data 
        results = books.bookrelcollection(book_id, collection_id, createdby)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchbookgenre(genre_id):
    try :
        message = ""    
        results = books.fetchbookgenre(genre_id)
        if not results:
             message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchbookgenremobile(genre_id):
    try :
        message = ""    
        results = books.fetchbookgenremobile(genre_id)
        if not results:
             message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Discuss():
    try :
        #GET DATA  
        book_id = request.form.get('book_id')
        user_id = request.form.get('user_id')
        title = request.form.get('title')
        isquestion = request.form.get('isquestion')
        topic = request.form.get('topic')
        createdby = request.form.get('createdby')
        isactive = request.form.get('isactive')
        # Insert data 
        results = books.discuss(book_id, user_id, title, isquestion, topic, createdby, isactive)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

def Deletediscuss(book_discuss_id):
    try :    
        results = books.deletediscuss(book_discuss_id)

        if not results:
            return response.badRequest([], 'insert data error!!!')
        
        message = ""
        return response.ok(results, message)
    except Exception as e :
        print(e)


def Updatediscuss(book_discuss_id):
    try :
        #GET DATA  
        title = request.form.get('title')
        isquestion = request.form.get('isquestion')
        topic = request.form.get('topic')
        # Insert data 
        results = books.updatediscuss(title, isquestion, topic, book_discuss_id)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

def Updatepostdiscuss(book_discuss_id):
    try :
        #GET DATA  
        created = request.form.get('created')
        post = request.form.get('post')
        

        # Insert data 
        results = books.updatepostdiscuss(created, post, book_discuss_id)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Booksfollowdiscuss():
    try :
        #GET DATA  
        user_id = request.form.get('user_id')
        book_discuss_id = request.form.get('book_discuss_id')
        createdby = request.form.get('createdby')

        # Insert data 
        results = books.booksfollowdiscuss(user_id, book_discuss_id, createdby)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

def Updatebooksrelrateuser():
    try :
        #GET DATA  
        book_id = request.form.get('book_id')
        rate = request.form.get('rate')
        user_id = request.form.get('user_id')

        # Insert data 
        results = books.updatebooksrelrateuser(book_id, rate, user_id)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

