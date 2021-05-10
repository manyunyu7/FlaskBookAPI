from app.models import master
from app import response, app
from flask import request
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)

@jwt_required
def Byid(table, data):
    try :
        message = ""    
        results = master.byid(table, data)
        if not results:
             message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Tableview(table, data):
    try :
        message = ""
        results = master.tableviewrow(table, data)
        
        if not results:
             message = "empty"

        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Tableviewresult(table, data, orderby):
    try :
        message = ""
        results = master.tableviewresult(table, data, orderby)
        
        if not results:
             message = "empty"

        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchdata(table, data, orderby):
    try :
        message = ""
        results = master.fetchdataall(table, data, orderby)

        if not results:
            message = "empty"

        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchall(table):
    try :
        message = ""
        results = master.fetchalldata(table)

        if not results:
            message = "empty"

        return response.ok(results, message)
    except Exception as e :
        print(e)


@jwt_required
def Fetchcondition(table, data):
    try :
        message = ""
        results = master.fetchcodition(table, data)
        
        if not results:
             message = "empty"

        return response.ok(results, message)
    except Exception as e :
        print(e)


@jwt_required
def Fetchconditionhighlight(table, data):
    try :
        message = ""
        results = master.fetchconditionhighlight(table, data)
        
        if not results:
             message = "empty"

        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchorderby(table, orderby):
    try :
        message = ""
        results = master.fetchorderby(table, orderby)
        
        if not results:
             message = "empty"

        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Callstoredprocedure(query):
    try :
        message = ""
        results = master.callstoredprocedure(query)
        
        if not results:
             message = "empty"

        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchallmenu():
    try :
        message = ""
        results = master.fetchallmenu()
        
        if not results:
             message = "empty"

        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchmymessagelist(id):
    try :
        message = ""
        results = master.fetchmymessagelist(id)
        
        if not results:
             message = "empty"

        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchmynotif(data):
    try :
        message = ""
        results = master.fetchmynotif(data)
        
        if not results:
             message = "empty"

        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchmynotiflimit(data, rowperpage, row):
    try :
        message = ""
        results = master.fetchmynotiflimit(data, rowperpage, row)
        
        if not results:
             message = "empty"

        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchcontentbymenu(data):
    try :
        message = ""
        results = master.fetchcontentbymenu(data)
        
        if not results:
             message = "empty"

        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchsidebartbl(data):
    try :
        message = ""
        results = master.fetchsidebartbl(data)
        
        if not results:
             message = "empty"

        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Insert():
    try :    
        table = request.form.get('table')
        column = request.form.get('column')
        data = request.form.get('data')
        

        results = master.insert(table, column, data)

        if not results:
            return response.badRequest([], 'insert data error!!!')
        
        message = ""
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Delete(table, data):
    try :    
        results = master.delete(table, data)

        if not results:
            return response.badRequest([], 'insert data error!!!')
        
        message = ""
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchroleadm():
    try :
        message = ""    
        results = master.fetchroleadm()
        if not results:
             message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchroleadmuserbyid(user_id):
    try :
        message = ""    
        results = master.fetchroleadmuserbyid(user_id)
        if not results:
             message = "empty"
        return response.ok(results, message)
    except Exception as e :
        print(e)