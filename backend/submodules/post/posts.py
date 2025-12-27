from flask import Flask, Blueprint, render_template, request
import sqlite3
posts = Blueprint('posts', __name__, template_folder="../template")
@posts.route('/posts', methods=["GET"])
def function_name():
    database = sqlite3.connect("../database/cyber.db")
    cursor = database.cursor()
    # cursor.execute("SELECT title, body FROM posts")
    # posts_items = cursor.fetchall()
    return render_template("/post/posts.html")