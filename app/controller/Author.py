from flask import request
from app import response, app
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from app.models import users

def Authorgenre(user_id):
    try:
        message = ""
        results = users.authorgenre(user_id)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e:
        print(e)

def Authorjobdesc(user_id):
    try:
        message = ""
        results = users.authorjobdesc(user_id)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e:
        print(e)

def FetchAllAuthorFollowed(user_id):
    try:
        message = ""
        results = users.fetchAllAuthorFollowed(user_id)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e:
        print(e)

@jwt_required
def Authorrellabel(table, i, name):
    try:
        message = ""
        results = users.authorrellabel(table, i, name)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e:
        print(e)

@jwt_required
def Authorrellabelbyid(i, book_id):
    try:
        message = ""
        results = users.authorrellabelbyid(i, book_id)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e:
        print(e)

@jwt_required
def Fetchallauthor():
    try:
        message = ""
        results = users.fetchallauthor()
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e:
        print(e)

@jwt_required
def Labels():
    try:
        message = ""
        results = users.labels()
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e:
        print(e)

@jwt_required
def Totalreader(reader, authorid):
    try:
        message = ""
        results = users.totalreader(reader, authorid)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e:
        print(e)

@jwt_required
def Usersosmedbyid(user_id):
    try:
        message = ""
        results = users.usersosmedbyid(user_id)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e:
        print(e)

@jwt_required
def Following(id, data):
    try:
        message = ""
        results = users.following(id, data)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e:
        print(e)

@jwt_required
def Followers(id, data):
    try:
        message = ""
        results = users.followers(id, data)
        if not results:
            message = "empty"
        return response.ok(results, message)
    except Exception as e:
        print(e)


@jwt_required
def Creatorprofession():
    try :
        #GET DATA  
        name = request.form.get('name')
        isactive = request.form.get('isactive')

        # Insert data 
        results = users.creatorprofession(name, isactive)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)


@jwt_required
def Userauthorrelposition():
    try :
        #GET DATA  
        books_rel_author_id = request.form.get('books_rel_author_id')
        position_id = request.form.get('position_id')

        # Insert data 
        results = users.userauthorrelposition(books_rel_author_id, position_id)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchonecreator():
    try:
        results = users.fetchonecreator()
        if not results:
            return response.badRequest([], 'add data error!!!')
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchsixcreator(id):
    try:
        results = users.fetchsixcreator(id)
        if not results:
            return response.badRequest([], 'add data error!!!')
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)