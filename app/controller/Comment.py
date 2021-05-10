from flask import request
from app import response, app
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from app.models import comments

@jwt_required
def Comment():
    try :
        #GET DATA  
        type = request.form.get('type')
        type_id = request.form.get('type_id')
        user_id = request.form.get('user_id')
        comment = request.form.get('comment')
        createdby = request.form.get('createdby')
        isactive = request.form.get('isactive')

        # Insert data 
        results = comments.comment(type, type_id, user_id, comment, createdby, isactive)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Love():
    try :
        #GET DATA  
        type = request.form.get('type')
        type_id = request.form.get('type_id')
        user_id = request.form.get('user_id')

        # Insert data 
        results = comments.loves(type, type_id, user_id)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)