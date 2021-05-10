from flask import request
from app import response, app
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from app.models import feeds

@jwt_required
def Feed():
    try :
        #GET DATA  
        user_id = request.form.get('user_id')
        feed = request.form.get('feeds')
        isactivity = request.form.get('isactivity')
        ispublic = request.form.get('ispublic')
        createdby = request.form.get('createdby')
        type = request.form.get('type')
        typeData = request.form.get('typeData')

        # Insert data 
        results = feeds.feed(user_id, feed, isactivity, ispublic, createdby, type, typeData)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Mentionfeed():
    try :
        #GET DATA  
        feed_id = request.form.get('feed_id')
        datatype = request.form.get('datatype')
        dataid = request.form.get('dataid')

        # Insert data 
        results = feeds.mentionfeed(feed_id, datatype, dataid)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)  