from flask import Flask,Blueprint,render_template,request
import sqlite3
ctf_id = Blueprint('ctf_id', __name__,template_folder="../template")    
@ctf_id.route('/ctf/<id>', methods=["GET","POST"])
def function_name(id):  
    print(id)  
    database = sqlite3.connect("../database/cyber.db")
    cursor = database.cursor()
    cursor.execute("SELECT title, description, points,img,ip FROM ctf_challenges WHERE id=?", (id,))
    ctf_item = cursor.fetchall()
    return render_template("/game/ctf_id.html", ctf=ctf_item)