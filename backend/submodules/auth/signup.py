from flask import Blueprint,render_template,request,redirect,url_for,session
from extension import bcrypt
import sqlite3

signup = Blueprint('signup', __name__,template_folder="../template")

@signup.route('/signup',methods=["POST","GET"])
def function_name():
    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        database = sqlite3.connect("../database/cyber.db")
        cursor = database.cursor()
        hash = bcrypt.generate_password_hash(password).decode()
        cursor.execute("INSERT INTO users (email,username,password)  VALUES(?,?,?)",(email,username,hash))
        cursor.execute("INSERT INTO security (username,ctf_point,courses_completed,level,ctf_completed) VALUES(?,?,?,?,?)",(username,0,0,"Beginner",0))
        database.commit()
        session['username'] = username
        return  redirect('/dashboard')
    return render_template("/auth/signup.html")      