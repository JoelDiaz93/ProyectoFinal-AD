from facebook_scraper import get_posts
import pypyodbc
import time

'''===============CONEXION=============='''
connection = pypyodbc.connect('Driver={SQL Server};Server=DESKTOP-541R5S3\SQLEXPRESS;Database=JUEGOSENLINEA;')
cursor = connection.cursor()

'''===============BUSQUEDA EN FACEBOOK=============='''
i = 1
for post in get_posts('FortniteES', pages=100, extra_info=True):
    print(i)
    i = i + 1
    time.sleep(1)
    mydate = post['time']

    try:
        SQLCommand = ("INSERT INTO cuba(id_post, texto, date, likes, comments, shares, reactions, url_post) VALUES (?,?,?,?,?,?,?,?)")
        Values = [post['post_id'], post['text'], mydate.timestamp(), post['likes'], post['comments'], post['shares'], post['reactions'], post['post_url']]
        cursor.execute(SQLCommand, Values)
        connection.commit()
        print("guardado exitosamente")

    except Exception as e:
        print("no se pudo grabar:" + str(e))

connection.close()