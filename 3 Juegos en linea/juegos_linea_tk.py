import couchdb
from TikTokApi import TikTokApi
import json

'''========couchdb'=========='''
server = couchdb.Server('http://admin:Joel$2021*@localhost:5984/')
try:
    # Nombre de la base de datos por provincia
    db = server.create('juegos_ec')
except:
    db = server['juegos_ec']

# Instancia de la api
api = TikTokApi.get_instance()
# Terminos de busqueda
search_term = ["fornite", "Ecuador"]

tiktoks = api.search_for_hashtags(search_term, count=30)

for tiktok in tiktoks:
    doc = db.save(tiktok)
    print(tiktok)
