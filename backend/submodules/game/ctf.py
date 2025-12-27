from flask import Blueprint, render_template, request
import sqlite3
ctf = Blueprint('ctf', __name__)      
@ctf.route('/ctf', methods=["GET","POST"])
def function_name():    
    database = sqlite3.connect("../database/cyber.db")
    cursor = database.cursor()
    cursor.execute("SELECT title, description, points,img,id FROM ctf_challenges")
    ctf_items = cursor.fetchall()
    return render_template("/game/ctf.html", ctf=ctf_items)