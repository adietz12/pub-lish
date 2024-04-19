#Create mongita database with article information
import json
from mongita import MongitaClientDisk  

#This one is for dates
from datetime import datetime
# Function to convert date string to datetime object
def convert_date(date_str):
    # Assuming the date format is 'month/day/year'
    month, day, year = map(int, date_str.split('/'))
    return datetime(year, month, day)

#Put future articles in here the way it is formatted
publish_data = [
    {"pop":"1","author":"Spongebob", "title":"How I lost my edging streak", "text":"blah blah blah blah", "date_created":convert_date("3/1/23"), "date_string":"3/1/23"},
    {"pop":"1","author":"Senator Armstrong", "title":"Why sigma male is better than alpha male", "text":"blah blah blah blah", "date_created":convert_date("5/28/19"), "date_string":"5/28/19"},
    {"pop":"1","author":"William Afton", "title":"My Skibidi Toilet addiction", "text":"blah blah blah blah", "date_created":convert_date("4/20/24"), "date_string":"4/20/24"},
    {"pop":"1","author":"Guts", "title":"I MET KAI CENAT!! (GONE SEXUAL)", "text":"blah blah blah blah", "date_created":convert_date("1/11/22"), "date_string":"1/11/22"}
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