#Use this command to run
#flask --app publish run
#This turns on debug mode
#flask --app publish --debug run
from flask import Flask, render_template, request, make_response, redirect, url_for
from mongita import MongitaClientDisk
from bson import ObjectId


app = Flask(__name__)

client = MongitaClientDisk()
#Open the articles database
articles_db = client.articles_db


@app.route("/", methods=["GET"])
def start():
    return render_template("home.html")

@app.route("/new_user")
def new_user():
    return render_template("new_user.html")

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
        data["id"] = str(data["_id"])
        return render_template("article.html", data=data)
    else:
        return redirect(url_for("start"))

@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")

@app.route("/log_in")
def log_in():
    return render_template("log_in.html")

@app.route("/home")
def home():
    return render_template("home.html")
