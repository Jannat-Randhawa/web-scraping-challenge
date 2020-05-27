#Dependencies 
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app)

@app.route("/")
def index(): 
    
    mars_info = mongo.db.mars_info.find_one()