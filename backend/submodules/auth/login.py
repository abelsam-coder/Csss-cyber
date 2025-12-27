from flask import Blueprint,render_template,request,session
from extension import bcrypt
import sqlite3

login = Blueprint('login', __name__)

@login.route('/login',methods=["POST","GET"])
def function_name():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hash = bcrypt.generate_password_hash(password).decode()
        database = sqlite3.connect("../database/cyber.db")
        cursor = database.cursor()
        cursor.execute("SELECT password FROM users WHERE username=?",(username,))
        password_verify = cursor.fetchone()
        if password_verify[0] and bcrypt.check_password_hash(password_verify[0], password):
            session['username'] = username
            return render_template("/auth/login.html",message="success",username=username,hash=hash)

        else:
            return render_template("/auth/login.html",message="failed")
    return render_template("/auth/login.html")