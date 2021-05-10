from flask import request
from app import response, app
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from app.models import collections

@jwt_required
def Collection():
    try :
        #GET DATA  
        name = request.form.get('name')
        user_id = request.form.get('user_id')
        description = request.form.get('description')
        isactive = request.form.get('isactive')
        ispublic = request.form.get('ispublic')
        createdby = request.form.get('createdby')

        # Insert data 
        results = collections.collection(name, user_id, description, isactive, ispublic, createdby)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

def Updatecollection(collection_id):
    try :
        #GET DATA  
        name = request.form.get('name')
        user_id = request.form.get('user_id')
        description = request.form.get('description')
        isactive = request.form.get('isactive')
        ispublic = request.form.get('ispublic')
        createdby = request.form.get('createdby')

        # update data 
        results = collections.updatecollection(name, user_id, description, isactive, ispublic, createdby, collection_id)

        #Cek data
        if not results:
            return response.badRequest([], 'update data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

def Updatefavoritecollection(collection_id):
    try :
        #GET DATA  
        isfavorite = request.form.get('isfavorite')
        order_position_fav = request.form.get('order_position_fav')

        # update data 
        results = collections.updatefavoritecollection(isfavorite, order_position_fav, collection_id)

        #Cek data
        if not results:
            return response.badRequest([], 'update data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)