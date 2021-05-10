from app.models import users
from flask import request
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, jwt_refresh_token_required, create_refresh_token, get_jwt_identity)
from app import response
import datetime, re

def Login():
    try :    
        usrnm = request.form.get('username')
        password = request.form.get('password')

        username = ""
        email = ""

        email_regex = re.search("@",usrnm)
        if not email_regex:
            username = "%"+usrnm+"%"
        else :
            email = "%"+usrnm+"%"

        results = users.fetchbysignin(username, email, password)

        if not results:
            message = "username or password wrong!!!"
            return response.unauthorised(results, message)
        else:
            expires = datetime.timedelta(days=1)
            expires_refresh = datetime.timedelta(days=3)
            access_token = create_access_token(results, fresh=True, expires_delta=expires)
            refresh_token = create_refresh_token(results, expires_delta=expires_refresh)
            return response.ok({
                "data": results,
                "token_access": access_token,
                "token_refresh": refresh_token,
            }, "")

    except Exception as e :
        print(e)

def Komiqus():
    try:
        id_key = '7a2548809b66e8763121abdb19a152c6'
        sckey = '1b44463e4e5412ee1406e0b42e4bcf18'

        app_id = request.form.get("app_id")
        securitykey = request.form.get("securitykey")

        if id_key == app_id :
            if sckey == securitykey :
                results = "Website-Komiqus"
                expires = datetime.timedelta(days=1)
                access_token = create_access_token(results, fresh=True, expires_delta=expires)
            else :
                return response.badRequest([], 'OUT!!!')
        else :
            return response.badRequest([], 'OUT!!!')
        
        return response.ok(access_token,"")
    except Exception as e :
            print(e)

@jwt_refresh_token_required
def refresh():
    try:
        user = get_jwt_identity()
        new_token = create_access_token(identity=user, fresh=False)

        return response.ok({
            "token_access": new_token
        }, "")

    except Exception as e:
        print(e)