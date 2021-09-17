from facebook_scraper import get_posts
from pymongo import MongoClient
import time
from pymongo.errors import ConnectionFailure

CLIENT = MongoClient("mongodb://localhost:27017/")
try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)
db = CLIENT["NoticiasInternacionales"]
facebook = db["prueba"]

i = 1
for post in get_posts('RosyMcMichael', pages=3, extra_info=True):
    print(i)
    i = i + 1
    time.sleep(1)

    id = post['post_id']
    doc = {}

    doc['id'] = id

    mydate = post['time']

    try:
        doc['likes'] = post['likes']
        doc['comments'] = post['comments']
        doc['shares'] = post['shares']
        doc['texto'] = post['text']
        doc['date'] = mydate.timestamp()

        try:
            doc['reactions'] = post['reactions']
        except:
            doc['reactions'] = {}

        doc['post_url'] = post['post_url']
        x = facebook.insert_one(doc)

        print("guardado exitosamente")

    except Exception as e:
        print("no se pudo grabar:" + str(e))