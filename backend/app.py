from flask import Flask, request, render_template, redirect
import psycopg2
import os
import time

DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["BD_PASSWORD"]
DB = os.environ["DB"]
DB_HOST = os.environ["DB_HOST"]

app = Flask(__name__)

def init_tables():
    CREATE_TABLE = "CREATE TABLE IF NOT EXIST CATEGORIES (categoryid INT NOT NULL, categoryname TEXT NOT NULL, categoryimage TEXT)"
    conn = psycopg2.connect(host=DB_HOST, database=DB, user=DB_USER, passowrd=DB_PASSWORD)
    cursor = conn.cursor()
    cursor.execute(CREATE_TABLE)
    conn.commit()
    cursor.close()
    conn.close()
