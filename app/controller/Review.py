from flask import request
from app import response, app
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from app.models import reviews

@jwt_required
def Review():
    try :
        #GET DATA  
        book_id = request.form.get('book_id')
        user_id = request.form.get('user_id')
        title = request.form.get('title')
        rate = request.form.get('rate')
        review = request.form.get('review')
        createdby = request.form.get('createdby')

        # Insert data 
        results = reviews.review(book_id, user_id, title, rate, review, createdby)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

def Updatereview(id):
    try :
        #GET DATA  
        title = request.form.get('title')
        rate = request.form.get('rate')
        review = request.form.get('review')

        # Insert data 
        results = reviews.updatereview(title, rate, review, id)

        #Cek data
        if not results:
            return response.badRequest([], 'update data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

def Ratereview():
    try :
        #GET DATA  
        book_id = request.form.get('book_id')
        user_id = request.form.get('user_id')
        rate = request.form.get('rate')

        # Insert data 
        results = reviews.ratereview(book_id, user_id, rate)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)