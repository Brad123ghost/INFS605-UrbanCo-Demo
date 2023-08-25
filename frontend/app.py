from flask import Flask, request, render_template, redirect
import requests
import os

class Review(object):
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

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
    return render_template("/categories.html")
app.run(host="0.0.0.0", port=5000)