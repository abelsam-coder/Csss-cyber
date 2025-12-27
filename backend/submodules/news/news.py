from flask import Blueprint, render_template, request
import sqlite3
news = Blueprint('news', __name__)      
@news.route('/news', methods=["GET"])
def function_name():    
    database = sqlite3.connect("../database/cyber.db")
    cursor = database.cursor()
    cursor.execute("SELECT title, content FROM news")
    news_items = cursor.fetchall()
    return render_template("/news/news.html", news=news_items)