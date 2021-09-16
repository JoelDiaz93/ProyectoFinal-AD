import requests
import pandas as pd
from bs4 import BeautifulSoup
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)


def find_1st(string, substring):
    return string.find(substring, string.find(substring))


response = requests.get("https://www.elcomercio.com/tag/juegos-olimpicos/")
soup = BeautifulSoup(response.content, features="lxml")

titulos = []
contenidos = []
ListSearch = []

titulos_post = soup.find_all("h3")
contenido_post = soup.find_all("p")

'''post_course=soup.find_all("span", class_="text-1 weight-semi line-tight")
post_provider=soup.find_all("a", class_="color-charcoal italic")'''

extracted = []
for element in titulos_post:
    # print(element)
    element = str(element)
    limpio = str(element[find_1st(element, '>') + 1:find_2nd(element, '<')])
    # print(limpio)
    titulos.append({"Content": limpio.strip()})

for element in contenido_post:
    # print(element)
    element = str(element)
    limpio = str(element[find_1st(element, '>') + 1:find_2nd(element, '<')])
    # print(limpio)
    contenidos.append({"Content": limpio.strip()})

dfDS=pd.DataFrame({'titulo':titulos, 'contenido':contenidos})

num=len(titulos)
for n in num:
    SQLCommand = ("INSERT INTO cuba(id_post, texto, date, likes, comments, shares, reactions, url_post) VALUES (?,?,?,?,?,?,?,?)")
    Values = [post['post_id'], post['text'], mydate.timestamp(), post['likes'], post['comments'], post['shares'],
              post['reactions'], post['post_url']]
    cursor.execute(SQLCommand, Values)
    connection.commit()

CLIENT = MongoClient("mongodb://localhost:27017/")
try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)
db = CLIENT["python"]
noticias = db["juegosolimpicos"]

insert = noticias.insert_many(dfDS)