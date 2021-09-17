import couchdb
from TikTokApi import TikTokApi

'''========CONEXION COUCHDB'=========='''
server = couchdb.Server('http://admin:Joel$2021*@localhost:5984/')
try:
    db = server.create('juegos_ec')
except:
    db = server['juegos_ec']

'''===============INSTANCIA A LA API=============='''
api = TikTokApi.get_instance()

'''===============TERMINOS DE BUSQUEDA=============='''
search_term = ["fornite", "Ecuador"]
tiktoks = api.search_for_hashtags(search_term, count=30)

'''===============INSERCION DE DATOS=============='''
for tiktok in tiktoks:
    doc = db.save(tiktok)
    print(tiktok)
