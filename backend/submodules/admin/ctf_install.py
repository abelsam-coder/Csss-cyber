from flask import Flask, Blueprint, render_template, request
import sqlite3
import uuid
import base64
ctf_install = Blueprint('ctf_install', __name__, template_folder="../template") 
@ctf_install.route('/ctf_install', methods=["GET","POST"])
def function_name():
    if request.method == "POST":
        title = request.form['title']
        description = request.form['description']
        image = request.files['image']
        ip = request.form["ip"]
        points = request.form['point']
        id = str(uuid.uuid4())
        encode = base64.b64encode(image.read()).decode()
        html_embed = f'data:image/png;base64,{encode}'
        database = sqlite3.connect("../database/cyber.db")
        cursor = database.cursor()
        cursor.execute("INSERT INTO ctf_challenges (title, description, points,img,id,ip) VALUES(?,?,?,?,?,?)",(title,description,points,html_embed,id,ip))
        database.commit()
        return "CTF Challenge Installed Successfully"
    return render_template("/admin/ctf_install.html")