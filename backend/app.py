from flask import Flask, request, render_template, redirect
import psycopg2
import os
import time

DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASS"]
DB = os.environ["DB"]
DB_HOST = os.environ["DB_HOST"]

app = Flask(__name__)

def init_tables():
    CREATE_TABLE = "CREATE TABLE IF NOT EXISTS CATEGORIES (categoryid serial PRIMARY KEY, categoryname TEXT NOT NULL, categoryimage TEXT)"
    conn = psycopg2.connect(host=DB_HOST, database=DB, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()
    cursor.execute(CREATE_TABLE)
    conn.commit()
    cursor.close()
    conn.close()

def load_categories():
    
    categories = []
    
    LOAD_CATEGORY = "SELECT * FROM CATEGORIES"
    conn = psycopg2.connect(host=DB_HOST, database=DB, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()
    cursor.execute(LOAD_CATEGORY)
    results = cursor.fetchall()

    for row in results:
        categories.append((row[0], row[1], row[2]))
    cursor.close()
    conn.close()

    return categories

@app.route("/categories/list", methods=["POST"])
def listcategories():
    
    categories = load_categories()
    
    return {"success":True, "list":categories}

time.sleep(20)
init_tables()
app.run(host="0.0.0.0", port=5000)