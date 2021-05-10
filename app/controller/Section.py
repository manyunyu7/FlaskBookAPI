from flask import request
from app import response, app
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from app.models import sections

@jwt_required
def Fetchcontenttbl(data):
    try :
        #GET DATA  
        results = sections.fetchcontenttbl(data)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Sectionbook():
    try :
        #GET DATA  
        name = request.form.get('name')
        description = request.form.get('description')
        type = request.form.get('type')
        algo_name = request.form.get('algo_name')
        isactive = request.form.get('isactive')
        createdby = request.form.get('createdby')

        # Insert data 
        results = sections.sectionbook(name, description, type, algo_name, isactive, createdby)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

def Updatesectionbook(section_id):
    try :
        #GET DATA  
        name = request.form.get('name')
        description = request.form.get('description')
        type = request.form.get('type')
        algo_name = request.form.get('algo_name')
        isactive = request.form.get('isactive')
        createdby = request.form.get('createdby')

        # Insert data 
        results = sections.updatesectionbook(name, description, type, algo_name, isactive, createdby, section_id)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Sectionbooklist():
    try :
        #GET DATA  
        section_id = request.form.get('section_id')
        book_id = request.form.get('book_id')
        addedby = request.form.get('addedby')

        # Insert data 
        results = sections.sectionbooklist(section_id, book_id, addedby)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

def Sectionbookcontent(section_id):
    try :
        #GET DATA  
        name = request.form.get('name')
        type = request.form.get('type')
        algo_name = request.form.get('algo_name')
        description = request.form.get('description')
        editedby = request.form.get('editedby')

        # Update data 
        results = sections.sectionbookcontent(name, description, type, algo_name, editedby, section_id)

        #Cek data
        if not results:
            return response.badRequest([], 'update data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Sidebar():
    try :
        #GET DATA  
        belongsto = request.form.get('belongsto')
        order_position = request.form.get('order_position')
        section_id = request.form.get('section_id')
        isactive = request.form.get('isactive')
        layout = request.form.get('layout')

        # Insert data 
        results = sections.sidebar(belongsto, order_position, section_id, isactive, layout)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)


def Updatesidebar():
    try :
        #GET DATA  
        belongsto = request.form.get('belongsto')
        isactive = request.form.get('isactive')
        layout = request.form.get('layout')
        sidebar_id = request.form.get('sidebar_id')

        # Insert data 
        results = sections.updatesidebar(belongsto, isactive, layout, sidebar_id)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

def Positionsidebar(sidebar_id):
    try :
        #GET DATA  
        order_position = request.form.get('order_position')

        # Insert data 
        results = sections.positionsidebar(order_position, sidebar_id)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

def Contenttbl(content_id):
    try :
        #GET DATA  
        isactive = request.form.get('isactive')
        layout = request.form.get('layout')
        belongsto = request.form.get('belongsto')

        # Insert data 
        results = sections.contenttbl(isactive, layout, belongsto, content_id)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

def Positioncontent(content_id):
    try :
        #GET DATA  
        order_position = request.form.get('order_position')

        # Insert data 
        results = sections.positioncontent(order_position, content_id)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)
