import app
import pymysql.cursors

def getConnection():
    #  Hosting
    # You can change the connection arguments.
    # connection = pymysql.connect(host='node27408-komiqus-dev-8.kilatiron.com',
    #                              user='u7887_super',
    #                              password='bookee7887KOMIDB',                             
    #                              db='u6507668_komiqusdb',
    #                              charset='utf8',
    #                              cursorclass=pymysql.cursors.DictCursor)

    # Local
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',                             
                                db='komiqus-new',
                                charset='utf8',
                                cursorclass=pymysql.cursors.DictCursor)
    return connection