from flask import Flask, request, render_template, redirect
import requests
import os

class Category(object):
    def __init__(self, categoryid, categoryname, categoryimage):
        self.categoryid = categoryid
        self.categoryname = categoryname
        self.categoryimage = categoryimage

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        categories = request.form["categories"]
        
        res = requests.post("http://local:5000/categories")
        
        if res.status_code == 200:
            return redirect("/categories")
    
    return render_template("index.html")

@app.route("/categories", methods=["GET"])
def categories():
    
    res = requests.post("http://backend:5000/categories/list").json()
    categories = []
    
    for category in res["list"]:
        categories.append(Category(category[0],category[1],category[2]))
    
    return render_template("categories.html", categories=categories)



app.run(host="0.0.0.0", port=5000)