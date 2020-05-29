#Dependencies 
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mission_to_mars")

@app.route("/")
def index(): 
    
    mars_dict = mongo.db.mars_dict.find_one()

    return render_template("index.html", mars_dict = mars_dict)

@app.route("/scrape")
def scrape():

    mars_dict = scrape_mars.scrape()

    mongo.db.mars_dict.update({}, mars_dict, upsert=True)

    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)


     
