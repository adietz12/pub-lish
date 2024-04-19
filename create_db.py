#Create mongita database with article information
import json
from mongita import MongitaClientDisk  

#Put future articles in here the way it is formatted
publish_data = [
    {"author":"Spongebob", "title":"How I lost my edging streak", "text":"blah blah blah blah"},
    {"author":"Senator Armstrong", "title":"Why sigma male is better than alpha male", "text":"blah blah blah blah"},
    {"author":"William Afton", "title":"My Skibidi Toilet addiction", "text":"blah blah blah blah"},
    {"author":"Guts", "title":"I MET KAI CENAT!! (GONE SEXUAL)", "text":"blah blah blah blah"}
]

#Create a mongita client connection
client = MongitaClientDisk()

#Create article database
articles_db = client.articles_db

#Create articles collections
article_collection = articles_db.article_collection

#empty the collection
article_collection.delete_many({})

#Put the quotes in the database
article_collection.insert_many(publish_data)

#Check if articles are there
print(article_collection.count_documents({}))