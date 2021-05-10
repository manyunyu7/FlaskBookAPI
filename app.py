from flask import Flask
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity, get_raw_jwt) #inisialisasi JWT
from app.controller import Book, Auth, Author, Master, User, Feed, Collection, Comment, Love, Review, Section
from flask import request

app = Flask(__name__)

#ACCESS_TOKEN_JWT
app.config['SECRET_KEY'] = 'komiqus_RestfulApiq1w2e3r4t5'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
jwt = JWTManager(app)

# A storage engine to save revoked tokens. In production if
# speed is the primary concern, redis is a good bet. If data
# persistence is more important for you, postgres is another
# great option. In this example, we will be using an in memory
# store, just to show you how this might work. For more
# complete examples, check out these:
# https://github.com/vimalloc/flask-jwt-extended/blob/master/examples/redis_blacklist.py
# https://github.com/vimalloc/flask-jwt-extended/tree/master/examples/database_blacklist
blacklist = set()


# For this example, we are just checking if the tokens jti
# (unique identifier) is in the blacklist set. This could
# be made more complex, for example storing all tokens
# into the blacklist with a revoked status when created,
# and returning the revoked status in this call. This
# would allow you to have a list of all created tokens,
# and to consider tokens that aren't in the blacklist
# (aka tokens you didn't create) as revoked. These are
# just two options, and this can be tailored to whatever
# your application needs.
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist
    
@app.route('/')
def index():
    return "Welcome to api komiqus"

@app.route('/test')
def test():
    return "test success to api komiqus"

# ======== USER ========

@app.route('/api/v1/getuser/<user_id>')
def getuser(user_id):
    return User.Getuser(user_id)

@app.route('/api/v1/getuserbyemail/<email>')
def getuserbyemail(email):
    return User.Getuserbyemail(email)

# @app.route('api/v1/fetchmynotif?data=for_user_id/<user_id>')
# def fetchmynotif(user_id):
#     return User.Fetchmynotif(user_id)

@app.route('/api/v1/user', methods=['POST','PUT'])
def user():
    if request.method == 'POST':
        return User.User()
    else :
        user_id = request.args.get("id")
        return User.Updateuser(user_id)

@app.route('/api/v1/userupdatepic', methods=['POST','PUT'])
def usermobile():
    if request.method == 'POST':
        return User.Updateuserpic()
    else :
        user_id = request.args.get("id")
        return User.Updateuserpic(user_id)

@app.route('/api/v1/useradm/<user_id>', methods=['PUT'])
def useradm(user_id):
    return User.Useradm(user_id)

@app.route('/api/v1/systempass/<user_id>', methods=['PUT'])
def systempass(user_id):
    return User.Systempass(user_id)

@app.route('/api/v1/isactive/<user_id>', methods=['PUT'])
def isactive(user_id):
    return User.Isactive(user_id)

@app.route('/api/v1/lastlogon/<user_id>', methods=['PUT'])
def lastlogon(user_id):
    return User.Lastlogon(user_id)
    
@app.route('/api/v1/register', methods=['POST'])
def register():
    return User.Register()

@app.route('/api/v1/userrole', methods=['POST'])
def userrole():
    return User.Userrole()

@app.route('/api/v1/userauthor', methods=['POST'])
def userauthor():
    return User.Userauthor()

@app.route('/api/v1/userfollowauthor', methods=['POST'])
def userfollowauthor():
    return User.Userfollowauthor()

@app.route('/api/v1/userreqbook', methods=['POST'])
def userreqbook():
    return User.Userreqbook()

@app.route('/api/v1/usersosmed', methods=['POST'])
def usersosmed():
    return User.Usersosmed()

@app.route('/api/v1/usergenre', methods=['POST'])
def usergenre():
    return User.Usergenre()
    
@app.route('/api/v1/notif', methods=['POST','PUT'])
def notif():
    if request.method == 'POST' :
        return User.Notif()
    else :
        for_user_id = request.args.get('id')
        return User.Updatenotif(for_user_id)

@app.route('/api/v1/userscountersearch', methods=['POST','PUT'])
def userscountersearch():
    if request.method == 'POST' :
        return User.Userscountersearch()
    else :
        id = request.args.get("id")
        return User.Updateuserscountersearch(id)

@app.route('/api/v1/fetchbysignin/')
def fetchbysignin():
    return User.Fetchbysignin()

@app.route('/api/v1/fetchpeoplefollowdiscuss/<discuss_id>/<myid>')
def fetchpeoplefollowdiscuss(discuss_id, myid):
    return User.Fetchpeoplefollowdiscuss(discuss_id, myid)

# ======== AUTHOR ========
@app.route('/api/v1/authorgenre/<user_id>')
def authorgenre(user_id):
    return Author.Authorgenre(user_id)

@app.route('/api/v1/authorjobdesc/<user_id>')
def authorjobdesc(user_id):
    return Author.Authorjobdesc(user_id)
    
@app.route('/api/v1/authorfollowed/<user_id>')
def authorfollowed(user_id):
    return Author.FetchAllAuthorFollowed(user_id)

@app.route('/api/v1/authorrellabel')
def authorrellabel():
    table = request.args.get("table")
    i = request.args.get("id")
    name = request.args.get("name")
    return Author.Authorrellabel(table, i, name)

@app.route('/api/v1/authorrellabelbyid')
def authorrellabelbyid():
    i = request.args.get("id")
    book_id = request.args.get("book_id")
    return Author.Authorrellabelbyid(i, book_id)

@app.route('/api/v1/creatorprofession', methods=['POST'])
def creatorprofession():
    return Author.Creatorprofession()

@app.route('/api/v1/fetchallauthor')
def fetchallauthor():
    return Author.Fetchallauthor()

@app.route('/api/v1/labels')
def labels():
    return Author.Labels()

@app.route('/api/v1/totalreader/<reader>/<authorid>')
def totalreader(reader, authorid):
    return Author.Totalreader(reader, authorid)

@app.route('/api/v1/usersosmedbyid/<user_id>')
def usersosmedbyid(user_id):
    return Author.Usersosmedbyid(user_id)

@app.route('/api/v1/userauthorrelposition', methods=['POST'])
def userauthorrelposition():
    return Author.Userauthorrelposition()

@app.route('/api/v1/following')
def following():
    id = request.args.get("id")
    data = request.args.get("data")
    return Author.Following(id, data)

@app.route('/api/v1/followers')
def followers():
    id = request.args.get("id")
    data = request.args.get("data")
    return Author.Followers(id, data)

@app.route('/api/v1/fetchonecreator')
def fetchonecreator():
    return Author.Fetchonecreator()

@app.route('/api/v1/fetchsixcreator/<id>')
def fetchsixcreator(id):
    return Author.Fetchsixcreator(id)

# ======== BOOKS ========

@app.route('/api/v1/book', methods=['POST'])
def book():
    return Book.Book()

@app.route('/api/v1/authorbooks')
def authorbooks():
    table = request.args.get("table")
    i = request.args.get("id")
    name = request.args.get("name")
    return Book.Authorbook(table, i, name)

@app.route('/api/v1/authorbookscode')
def authorbookscode():
    table = request.args.get("table")
    i = request.args.get("id")
    name = request.args.get("name")
    code = request.args.get("code")
    return Book.Authorbookcode(table, i, name, code)

@app.route('/api/v1/authorinbook/<book_id>')
def authorinbook(book_id):
    return Book.Authorinbook(book_id)

@app.route('/api/v1/bookbycode/<code>')
def bookbycode(code):
    return Book.Bookbycode(code)

@app.route('/api/v1/bookbymyreq/<book_id>')
def bookbymyreq(book_id):
    return Book.Bookbymyreq(book_id)

@app.route('/api/v1/bookbygenre/<id_genre>')
def bookbygenre(id_genre):
    return Book.Bookbygenre(id_genre)

@app.route('/api/v1/bookbystatus')
def bookbystatus():
    data = request.args.get("data")
    return Book.Bookbystatus(data)

@app.route('/api/v1/bookforseries')
def bookforseries():
    data = request.args.get("data")
    return Book.Bookforseries(data)

@app.route('/api/v1/bookforcollection')
def bookforcollection():
    data = request.args.get("data")
    return Book.Bookforcollection(data)

@app.route('/api/v1/bookrelauthor', methods=['POST'])
def bookrelauthor():
    return Book.Bookrelauthor()

@app.route('/api/v1/bookrelcollection', methods=['POST'])
def bookrelcollection():
    return Book.Bookrelcollection()

@app.route('/api/v1/bookreluser')
def bookreluser():
    table = request.args.get("table")
    i = request.args.get("id")
    name = request.args.get("name")
    return Book.Bookreluser(table, i, name)

@app.route('/api/v1/bookreluserwatcher/<id>')
def bookreluserwatcher(id):
    table = request.args.get("table")
    i = request.args.get("id")
    name = request.args.get("name")
    return Book.Bookreluserwatcher(id, table, i, name)

@app.route('/api/v1/bookreluserseries/<series_id>')
def bookreluserseries(series_id):
    return Book.Bookreluserseries(series_id)

@app.route('/api/v1/bookcounterview', methods=['POST','PUT'])
def bookcounterview():
    if request.method == 'POST' :
        return Book.Bookcounterview()
    else :
        id = request.args.get("id")
        return Book.Updatebookcounterview(id)

@app.route('/api/v1/bookscountersearch', methods=['POST','PUT'])
def bookscountersearch():
    if request.method == 'POST' :
        return Book.Bookscountersearch()
    else :
        id = request.args.get("id")
        return Book.Updatebookscountersearch(id)

@app.route('/api/v1/bookrelgenre',methods=['POST', 'GET'])
def bookrelgenre():
    if request.method == 'GET':
        table = request.args.get("table")
        i = request.args.get("id")
        return Book.Bookrelgenre(table, i)
    else:
        return Book.Insertbookrelgenre()

@app.route('/api/v1/bookrellink', methods=['POST'])
def bookrellink():
    return Book.Bookrellink()

@app.route('/api/v1/bookseries', methods=['POST','PUT'])
def bookseries():
    if request.method == 'POST':
        return Book.Bookseries()
    else:
        return Book.Updatebookseries()
    

@app.route('/api/v1/bookrelseries', methods=['POST'])
def bookrelseries():
    return Book.Bookrelseries()

@app.route('/api/v1/bookrelstatususer', methods=['POST','PUT'])
def bookrelstatususer():
    if request.method == 'POST':
        return Book.Bookrelstatususer()
    else :
        return Book.Updatebookrelstatususer()

@app.route('/api/v1/booksrelrateuser', methods=['POST','PUT'])
def booksrelrateuser():
    if request.method == 'POST':
        return Book.Booksrelrateuser()
    else :
        return Book.Updatebooksrelrateuser()

@app.route('/api/v1/booklabel/<book_id>')
def booklabel(book_id):
    return Book.Booklabel(book_id)

@app.route('/api/v1/genresbook/<book_id>')
def genresbook(book_id):
    return Book.Genresbook(book_id)

@app.route('/api/v1/fetchbyrole')
def fetchbyrole():
    data = request.args.get("data")
    return Book.Fetchbyrole(data)

@app.route('/api/v1/fetchallrequest')
def fetchallrequest():
    return Book.Fetchallrequest()

@app.route('/api/v1/fetchallmyrequest/<id_user>')
def fetchallmyrequest(id_user):
    return Book.Fetchallmyrequest(id_user)

@app.route('/api/v1/fetchbookhasstatus/<book_id>/<id_user>')
def fetchbookhasstatus(book_id, id_user):
    return Book.Fetchbookhasstatus(book_id, id_user)

@app.route('/api/v1/fetchdiscuss')
def fetchdiscuss():
    id_user = request.args.get("id_user")
    data = request.args.get("data")
    return Book.Fetchdiscuss(id_user, data)

@app.route('/api/v1/discuss', methods=['POST','PUT'])
def discuss():
    if request.method == 'POST' :
        return Book.Discuss()
    else :
        book_discuss_id = request.args.get('id')
        return Book.Updatediscuss(book_discuss_id)

@app.route('/api/v1/deletediscuss/<book_discuss_id>', methods=['DELETE'])
def deletediscuss(book_discuss_id):
        return Book.Deletediscuss(book_discuss_id)

@app.route('/api/v1/postdiscuss/<book_discuss_id>', methods=['PUT'])
def postdiscuss(book_discuss_id):
    return Book.Updatepostdiscuss(book_discuss_id)

@app.route('/api/v1/booksfollowdiscuss', methods=['POST'])
def booksfollowdiscuss():
    return Book.Booksfollowdiscuss()

@app.route('/api/v1/fetchbookgenre/<genre_id>')
def fetchbookgenre(genre_id):
    return Book.Fetchbookgenre(genre_id)

@app.route('/api/v1/fetchbookgenremobile/<genre_id>')
def fetchbookgenremobile(genre_id):
    return Book.Fetchbookgenremobile(genre_id)

@app.route('/api/v1/fetchallactvdiscuss/<id_user>')
def fetchallactvdiscuss(id_user):
    return Book.Fetchallactvdiscuss(id_user)

@app.route('/api/v1/fetchallactvdiscussbyauthor/<author_id>')
def fetchallactvdiscussbyauthor(author_id):
    return Book.Fetchallactvdiscussbyauthor(author_id)

@app.route('/api/v1/fetchallactvdiscussbybook/<book_id>')
def fetchallactvdiscussbybook(book_id):
    return Book.Fetchallactvdiscussbybook(book_id)

@app.route('/api/v1/fetchallactvdiscussbybookfollow/<book_id>/<id_user>')
def fetchallactvdiscussbybookfollow(book_id, id_user):
    return Book.Fetchallactvdiscussbybookfollow(book_id, id_user)

@app.route('/api/v1/fetchallactvreviewbybook/<book_id>/<id_user>')
def fetchallactvreviewbybook(book_id, id_user):
    return Book.Fetchallactvreviewbybook(book_id, id_user)

@app.route('/api/v1/fetchallmydicuss/<id_user>')
def fetchallmydicuss(id_user):
    return Book.Fetchallmydicuss(id_user)

@app.route('/api/v1/fetchallmyseries')
def fetchallmyseries():
    data = request.args.get("data")
    return Book.Fetchallmyseries(data)

@app.route('/api/v1/fetchallcomment')
def fetchallcomment():
    id_user = request.args.get("id")
    data = request.args.get("data")
    return Book.Fetchallcomment(data, id_user)


@app.route('/api/v1/fetchcollectiondropdown/<book_id>/<id_user>')
def fetchcollectiondropdown(book_id, id_user):
    return Book.Fetchcollectiondropdown(book_id, id_user)

@app.route('/api/v1/fetchallmyactvcollection')
def fetchallmyactvcollection():
    data = request.args.get("data")
    return Book.Fetchallmyactvcollection(data)

@app.route('/api/v1/fetchallinmonth')
def fetchallinmonth():
    return Book.Fetchallinmonth()

@app.route('/api/v1/feedrow')
def feedrow():
    data = request.args.get("data")
    return Book.Feedrow(data)

@app.route('/api/v1/rate')
def rate():
    data = request.args.get("data")
    return Book.Rate(data)

@app.route('/api/v1/rateseries/<series_id>')
def rateseries(series_id):
    return Book.Rateseries(series_id)

@app.route('/api/v1/relbook')
def relbook():
    table = request.args.get("table")
    data = request.args.get("data")
    return Book.Relbook(table, data)

@app.route('/api/v1/reviwersbyuser')
def reviwersbyuser():
    user_id = request.args.get("id")
    data = request.args.get("data")
    return Book.Reviwersbyuser(user_id, data)

@app.route('/api/v1/relatecollectionbybook')
def relatecollectionbybook():
    data = request.args.get("data")
    return Book.Relatecollectionbybook(data)

@app.route('/api/v1/seriesbyid/<i>')
def seriesbyid(i):
    return Book.Seriesbyid(i)

@app.route('/api/v1/statusbookseries')
def statusbookseries():
    data = request.args.get("data")
    return Book.Statusbookseries(data)

@app.route('/api/v1/trandingbooks')
def trandingbooks():
    return Book.Trandingbooks()

@app.route('/api/v1/newrelease')
def newrelease():
    return Book.Newrelease()

@app.route('/api/v1/newreleasemobile')
def newreleasemobile():
    return Book.Newreleasemobile()

@app.route('/api/v1/lastaddbook/<id_user>')
def lastaddbook(id_user):
    return Book.Lastaddbook(id_user)

# ======= COMMENT ========
@app.route('/api/v1/comment', methods=['POST'])
def comment():
    return Comment.Comment()

# ======= COLLECTION ========
@app.route('/api/v1/collection', methods=['POST','PUT'])
def collection():
    if request.method == 'POST':
        return Collection.Collection()
    else :
        id = request.args.get("id")
        return Collection.Updatecollection(id)

@app.route('/api/v1/favoritecollection', methods=['PUT'])
def favoritecollection():
    collection_id = request.args.get("id")
    return Collection.Updatefavoritecollection(collection_id)

# ======== FEED ========
@app.route('/api/v1/feed', methods=['POST'])
def feed():
    return Feed.Feed()

@app.route('/api/v1/mentionfeed', methods=['POST'])
def mentionfeed():
    return Feed.Mentionfeed()

# ======== REVIEW ========
@app.route('/api/v1/review', methods=['POST','PUT'])
def review():
    if request.method == 'POST' :
        return Review.Review()
    else :
        id = request.args.get('id')
        return Review.Updatereview(id)

@app.route('/api/v1/ratereview', methods=['PUT'])
def ratereview():
    return Review.Ratereview()

# ======= LIKE ========
@app.route('/api/v1/love', methods=['POST'])
def love():
    return Love.Love()

# ======= SEARCH ========
@app.route('/api/v1/search')
def search():
    query = request.args.get("q")
    return Book.Search(query)

@app.route('/api/v1/searchmobile/<query>')
def searchmobile(query):
    return Book.Searchmobile(query)  

@app.route('/api/v1/searchbook')
def searchbook():
    query = request.args.get("q")
    return Book.Searchbook(query)

@app.route('/api/v1/searchseries')
def searchseries():
    query = request.args.get("q")
    return Book.Searchseries(query)

# ======== AUTH ========
@app.route('/api/v1/login', methods=['POST'])
def login():
    return Auth.Login()

@app.route('/api/v1/komiqus', methods=['POST'])
def komiqus():
    return Auth.Komiqus()

# ======== MASTER ========

@app.route('/api/v1/byid')
def byid():
    table = request.args.get("table")
    data = request.args.get("data")
    return Master.Byid(table, data)

@app.route('/api/v1/callstoredprocedure')
def callstoredprocedure():
    query = request.args.get("query")
    return Master.Callstoredprocedure(query)

@app.route('/api/v1/tableview')
def tableview():
    table = request.args.get("table")
    data = request.args.get("data")
    return Master.Tableview(table, data)

@app.route('/api/v1/tableviewresult')
def tableviewresult():
    table = request.args.get("table")
    data = request.args.get("data")
    orderby = request.args.get("orderby")
    return Master.Tableviewresult(table, data, orderby)

@app.route('/api/v1/fetchall')
def fetchall():
    table = request.args.get("table")
    return Master.Fetchall(table)

@app.route('/api/v1/fetchdata')
def fetchdata():
    table = request.args.get("table")
    data = request.args.get("data")
    orderby = request.args.get("orderby")
    return Master.Fetchdata(table, data, orderby)

@app.route('/api/v1/fetchcondition')
def fetchcondition():
    table = request.args.get("table")
    data = request.args.get("data")
    return Master.Fetchcondition(table, data)

@app.route('/api/v1/fetchconditionhighlight')
def fetchconditionhighlight():
    table = request.args.get("table")
    data = request.args.get("data")
    return Master.Fetchconditionhighlight(table, data)

@app.route('/api/v1/fetchorderby')
def fetchorderby():
    table = request.args.get("table")
    orderby = request.args.get("orderby")
    return Master.Fetchorderby(table, orderby)

@app.route('/refresh', methods=['POST'])
def refresh():
    return Auth.refresh()

# ======== SECTION ========
@app.route('/api/v1/fetchcontenttbl')
def fetchcontenttbl():
    data = request.args.get("data")
    return Section.Fetchcontenttbl(data)

@app.route('/api/v1/sectionbook', methods=['POST','PUT'])
def sectionbook():
    if request.method == 'POST':
        return Section.Sectionbook()
    else :
        section_id = request.args.get('id')
        return Section.Updatesectionbook(section_id)

@app.route('/api/v1/sectionbooklist', methods=['POST'])
def sectionbooklist():
    return Section.Sectionbooklist()

@app.route('/api/v1/sectionbookcontent/<section_id>', methods=['PUT'])
def sectionbookcontent(section_id):
   return Section.Sectionbookcontent(section_id)

# ======== SIDEBAR ========
@app.route('/api/v1/sidebar', methods=['POST','PUT'])
def sidebar():
    if request.method == 'POST':
        return Section.Sidebar()
    else:
        return Section.Updatesidebar()

@app.route('/api/v1/positionsidebar/<sidebar_id>', methods=['PUT'])
def positionsidebar(sidebar_id):
        return Section.Positionsidebar(sidebar_id)

# ======== CONTENT ========
@app.route('/api/v1/contenttbl/<content_id>', methods=['PUT'])
def contenttbl(content_id):
        return Section.Contenttbl(content_id)

@app.route('/api/v1/positioncontent/<content_id>', methods=['PUT'])
def positioncontent(content_id):
        return Section.Positioncontent(content_id)

# ======== OTHER ========

@app.route('/api/v1/fetchallmenu')
def fetchallmenu():
    return Master.Fetchallmenu()

@app.route('/api/v1/fetchmymessagelist/<id>')
def fetchmymessagelist(id):
    return Master.Fetchmymessagelist(id)

@app.route('/api/v1/fetchmynotif')
def fetchmynotif():
    data = request.args.get("data")
    return Master.Fetchmynotif(data)

@app.route('/api/v1/fetchmynotiflimit')
def fetchmynotiflimit():
    data = request.args.get("data")
    rowperpage = request.args.get("rowperpage")
    row = request.args.get("row")
    return Master.Fetchmynotiflimit(data, rowperpage, row)

@app.route('/api/v1/fetchcontentbymenu')
def fetchcontentbymenu():
    data = request.args.get("data")
    return Master.Fetchcontentbymenu(data)

@app.route('/api/v1/fetchsidebartbl')
def fetchsidebartbl():
    data = request.args.get("data")
    return Master.Fetchsidebartbl(data)

@app.route('/api/v1/fetchroleadm')
def fetchroleadm():
    return Master.Fetchroleadm()

@app.route('/api/v1/fetchroleadmuserbyid/<user_id>')
def fetchroleadmuserbyid(user_id):
    return Master.Fetchroleadmuserbyid(user_id)


@app.route('/api/v1/insert', methods=['POST'])
def insert():
    return Master.Insert()

@app.route('/api/v1/delete', methods=['DELETE'])
def delete():
    table = request.args.get('table')
    data = request.args.get('data')
    return Master.Delete(table, data)

# Endpoint for revoking the current users access token
@app.route('/api/v1/logout', methods=['DELETE'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return {"msg": "Successfully logged out"}

if __name__ == '__main__':
    app.run(host= '192.168.43.149')
    app.run()