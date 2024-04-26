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


#Put future articles in this array then just index it in the actual db so it doesn't clutter it up
article = ["""Greetings, fellow denizens of the plumbing world, it is I, William Afton, your humble co-founder of Freddy's Family Diner, here to regale you with tales from the front lines of the porcelain battleground. Today's topic? The insidious invasion of toilets with heads that seem to have a personal vendetta against my sanity.

Picture this: it's 2 AM, and while normal people are lost in the blissful embrace of slumber, I find myself lying awake, haunted by visions of lurking lavatories. Yes, you heard me right. Those porcelain demons have infiltrated my dreams, turning even my most peaceful nights into battlegrounds of terror.

It's not just during the witching hour, either. Oh no, these malevolent commodes have seeped into every facet of my existence. I'll be enjoying a leisurely stroll in the park, only to have my tranquility shattered by the sudden thought of a toilet with a grinning head popping out like a demented Jack-in-the-Box. Or I'll be savoring a slice of pizza at Freddy's, only for my mind to wander to the lurking horrors waiting in the restroom.

You see, it's not just a matter of encountering these cursed contraptions in the line of duty. They've insidiously woven themselves into the fabric of my consciousness, lurking in the shadows of my thoughts like malevolent specters. I can't escape them, no matter how hard I try.

Friends and family try to console me, offering words of comfort like, "It's just a toilet, William, nothing to be afraid of." But they don't understand. They don't know the sheer existential dread that comes from knowing that at any moment, a toilet with a head could be lurking just around the corner, ready to ambush me with its grotesque surprise.

So, my fellow plumbers, as we continue to wage our never-ending battle against leaky faucets and stubborn clogs, let us not forget the true horror that lurks in the depths of our beloved porcelain palaces. And if you ever find yourself lying awake at night, tormented by visions of toilets with heads, just know that you're not alone."""]
#Put future articles in here the way it is formatted
print(article)
publish_data = [
    {"pop":"1","author":"Spongebob", "title":"How I lost my edging streak", "text":"blah blah blah blah", "date_created":convert_date("3/1/23"), "date_string":"3/1/23"},
    {"pop":"1","author":"Senator Armstrong", "title":"Why sigma male is better than alpha male", "text":"blah blah blah blah", "date_created":convert_date("5/28/19"), "date_string":"5/28/19"},
    {"pop":"1","author":"William Afton", "title":"My Skibidi Toilet addiction", "text":article[0], "date_created":convert_date("4/20/24"), "date_string":"4/20/24"},
    {"pop":"1","author":"Guts", "title":"I MET KAI CENAT!! (GONE SEXUAL)", "text":"blah blah blah blah", "date_created":convert_date("1/11/22"), "date_string":"1/11/22"},
    {"pop":"1","author":"Spongebob", "title":"The best Grimace Shake flavor", "text":"blah blah blah blah", "date_created":convert_date("3/14/21"), "date_string":"3/14/21"}
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