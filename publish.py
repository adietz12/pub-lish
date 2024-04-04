#Use this command to run
#flask --app publish run
#This turns on debug mode
#flask --app publish --debug run
from flask import Flask, render_template, request, make_response, redirect
from mongita import MongitaClientDisk
from bson import ObjectId

app = Flask(__name__)

@app.route("/", methods=["GET"])
def start():
    return render_template("home.html")