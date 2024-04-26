#Use this command to run
#flask --app publish run
#This turns on debug mode
#flask --app publish --debug run
from flask import Flask, render_template, request, make_response, redirect, url_for
from mongita import MongitaClientDisk
from bson import ObjectId
import re


app = Flask(__name__)

client = MongitaClientDisk()
#Open the articles database
articles_db = client.articles_db


@app.route("/", methods=["GET"])
@app.route("/home")
def start():
    article_collection = articles_db.article_collection
    #Load featured
    featured = article_collection.find_one(sort=[("date_created", -1)])
    featured["_id"] = str(featured["_id"])
    featured["object"] = ObjectId(featured["_id"])
    
    #load data
    data = list(article_collection.find({}))
    for item in data:
        item["_id"] = str(item["_id"])
        item["object"] = ObjectId(item["_id"])
    return render_template("home.html", data=data, featured=featured, page="Home")


@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/feed")
def feed():
    article_collection = articles_db.article_collection
    #load data
    data = list(article_collection.find({}))
    for item in data:
        item["_id"] = str(item["_id"])
        item["object"] = ObjectId(item["_id"])
    return render_template("feed.html", data=data, page="Feed")

@app.route("/trending")
def trending():
    article_collection = articles_db.article_collection
    #load data
    data = list(article_collection.find({}).sort("pop", -1))
    for item in data:
        item["_id"] = str(item["_id"])
        item["object"] = ObjectId(item["_id"])
    return render_template("feed.html", data=data, page="Trending")

@app.route("/latest")
def latest():

    #Convert date strings to datetime objects in db
    article_collection = articles_db.article_collection

    #load data
    data = list(article_collection.find({}).sort("date_created", -1))
    for item in data:
        item["_id"] = str(item["_id"])
        item["object"] = ObjectId(item["_id"])
    return render_template("feed.html", data=data, page="Latest")

@app.route("/article/<id>", methods=["GET"])
def article(id=None):
    if id:
        #open data
        article_collection=articles_db.article_collection
        
        #get item
        data = article_collection.find_one({"_id": ObjectId(id)})
        print(data)
        data["id"] = str(data["_id"])
        return render_template("article.html", data=data)
    else:
        return redirect(url_for("start"))

@app.route("/search", methods=["POST"])
@app.route("/search", methods=["GET"])
def search():
    search_input = request.form.get("search-input", "")
    article_collection = articles_db.article_collection

    #Filter by dropdown option
    filter_by = request.form.get("filter", "title")

    if filter_by == "title":
        query = {"title": {"$eq": search_input}}
    elif filter_by == "author":
        query = {"author": {"$eq": search_input}}
    else:
        query={}
    # Query the database by exact title match
    data = list(article_collection.find(query))

    # Convert ObjectId to string for each document
    for item in data:
        item["_id"] = str(item["_id"])
        item["object"] = ObjectId(item["_id"])
    
    return render_template("search.html", data=data)

    
@app.route("/new_user")
def new_user():
    return render_template("new_user.html")
@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")
@app.route("/log_in")
def log_in():
    return render_template("log_in.html")
