from flask import request
from app import response, app
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from app.models import users

@jwt_required
def Getuser(user_id):
    try :
        results = users.getuser(user_id)
        if not results:
            return response.badRequest([], 'add users data error!!!')
                
        message = ""

        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Getuserbyemail(email):
    try :
        results = users.getuserbyemail(email)
        if not results:
            return response.badRequest([], 'add users data error!!!')
                
        message = ""

        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def User():
    try :
        #GET DATA  
        firstname = request.form.get('firstname')
        middlename = request.form.get('middlename')
        lastname = request.form.get('lastname')
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        biodata = request.form.get('biodata')
        birthdate = request.form.get('birthdate')
        place_birthdate = request.form.get('place_birthdate')
        gender = request.form.get('gender')
        country = request.form.get('country')
        city = request.form.get('city')
        province = request.form.get('province')
        phone = request.form.get('phone')
        isactive = request.form.get('isactive')
        picture = request.form.get('picture')
        createdby = request.form.get('createdby')
        editedby = request.form.get('editedby')

        # Insert data 
        results = users.user(firstname, middlename, lastname, username, password, email, biodata, birthdate, place_birthdate, gender, country, city, province, phone, isactive, picture, createdby, editedby)

        #Cek data
        if not results:
            return response.badRequest([], 'add users data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

def Updateuserpic(user_id):
    try :
        #GET DATA  
        picture = request.form.get('picture')

        # Insert data 
        results = users.updateuserpic(picture, user_id)

        #Cek data
        if not results:
            return response.badRequest([], 'Update users data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

def Updateuser(user_id):
    try :
        #GET DATA  
        firstname = request.form.get('firstname')
        middlename = request.form.get('middlename')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        biodata = request.form.get('biodata')
        birthdate = request.form.get('birthdate')
        place_birthdate = request.form.get('place_birthdate')
        gender = request.form.get('gender')
        country = request.form.get('country')
        city = request.form.get('city')
        province = request.form.get('province')
        phone = request.form.get('phone')
        picture = request.form.get('picture')
        editedby = request.form.get('editedby')

        # Insert data 
        results = users.updateuser(firstname, middlename, lastname, email, biodata, birthdate, place_birthdate, gender, country, city, province, phone, picture, editedby, user_id)

        #Cek data
        if not results:
            return response.badRequest([], 'Update users data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

def Useradm(user_id):
    try :
        #GET DATA  
        firstname = request.form.get('firstname')
        middlename = request.form.get('middlename')
        lastname = request.form.get('lastname')
        username = request.form.get('username')
        email = request.form.get('email')
        biodata = request.form.get('biodata')
        birthdate = request.form.get('birthdate')
        place_birthdate = request.form.get('place_birthdate')
        gender = request.form.get('gender')
        country = request.form.get('country')
        city = request.form.get('city')
        province = request.form.get('province')
        phone = request.form.get('phone')
        picture = request.form.get('picture')
        editedby = request.form.get('editedby')
        url_slug = request.form.get('url_slug')


        # Insert data 
        results = users.updateuseradm(firstname, middlename, lastname, username, email, biodata, birthdate, place_birthdate, gender, country, city, province, phone, picture, editedby, url_slug, user_id)

        #Cek data
        if not results:
            return response.badRequest([], 'Update users data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

def Isactive(user_id):
    try :
        #GET DATA  
        isactv = request.form.get('isactv')

        # Insert data 
        results = users.isactive(isactv, user_id)

        #Cek data
        if not results:
            return response.badRequest([], 'update users data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Systempass(user_id):
    try :
        #GET DATA  
        password = request.form.get('password')

        # Insert data 
        results = users.systempass(password, user_id)

        #Cek data
        if not results:
            return response.badRequest([], 'update users data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

def Lastlogon(user_id):
    try :
        #GET DATA  
        lastlogon = request.form.get('lastlogon')

        # Insert data 
        results = users.lastlogon(lastlogon, user_id)

        #Cek data
        if not results:
            return response.badRequest([], 'add users data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)


@jwt_required
def Register():
    try :
        #GET DATA  
        firstname = request.form.get('firstname')
        middlename = request.form.get('middlename')
        lastname = request.form.get('lastname')
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        isactive = request.form.get('isactive')
        url_slug = request.form.get('url_slug')
        createdby = request.form.get('createdby')

        # Insert data 
        results = users.register(firstname, middlename, lastname, username, password, email, isactive, url_slug, createdby)

        #Cek data
        if not results:
            return response.badRequest([], 'add users data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Userrole():
    try :
        #GET DATA  
        user_id = request.form.get('user_id')
        role_id = request.form.get('role_id')

        # Insert data 
        results = users.userrole(user_id, role_id)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchbysignin():
    try :
        #GET DATA  
        password = request.form.get('password')
        username = request.form.get('username')
        email = request.form.get('email')

        # Insert data 
        results = users.fetchbysignin(password, username, email)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Userauthor():
    try :
        #GET DATA  
        user_id = request.form.get('user_id')
        isapproved = request.form.get('isapproved')
        createdby = request.form.get('createdby')

        # Insert data 
        results = users.userauthor(user_id, isapproved, createdby)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Userfollowauthor():
    try :
        #GET DATA  
        user_id = request.form.get('user_id')
        author_id = request.form.get('author_id')

        # Insert data 
        results = users.userfollowauthor(user_id, author_id)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Userreqbook():
    try :
        #GET DATA  
        user_id = request.form.get('user_id')
        book_id = request.form.get('book_id')
        status = request.form.get('status')
        createdby = request.form.get('createdby')

        # Insert data 
        results = users.userreqbook(user_id, book_id, status, createdby)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Notif():
    try :
        #GET DATA  
        user_id = request.form.get('user_id')
        for_user_id = request.form.get('for_user_id')
        category = request.form.get('category')
        message = request.form.get('message')
        link = request.form.get('link')

        # Insert data 
        results = users.notif(user_id, for_user_id, category, message, link)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

def Updatenotif(for_user_id):
    try :
        # Update data 
        results = users.updatenotif(for_user_id)

        #Cek data
        if not results:
            return response.badRequest([], 'update data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Usersosmed():
    try :
        #GET DATA  
        user_id = request.form.get('user_id')
        sosmed_id = request.form.get('sosmed_id')

        # Insert data 
        results = users.usersosmed(user_id, sosmed_id)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Usergenre():
    try :
        #GET DATA  
        user_id = request.form.get('user_id')
        genre_id = request.form.get('genre_id')

        # Insert data 
        results = users.usergenre(user_id, genre_id)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Fetchpeoplefollowdiscuss(discuss_id, myid):
    try :
        #GET DATA  
        results = users.fetchpeoplefollowdiscuss(discuss_id, myid)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

@jwt_required
def Userscountersearch():
    try :
        #GET DATA  
        user_id = request.form.get('user_id')
        count = request.form.get('count')

        # Insert data 
        results = users.userscountersearch(user_id, count)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)

def Updateuserscountersearch(id):
    try :
        #GET DATA  
        user_id = request.form.get('user_id')
        count = request.form.get('count')

        # Insert data 
        results = users.updateuserscountersearch(user_id, count, id)

        #Cek data
        if not results:
            return response.badRequest([], 'add data error!!!')
        
        message = ""

        # Return data
        return response.ok(results, message)
    except Exception as e :
        print(e)