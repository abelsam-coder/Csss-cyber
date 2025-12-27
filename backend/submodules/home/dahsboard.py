from flask import Blueprint, render_template, request,session
import sqlite3
dashboard = Blueprint('dashboard', __name__, template_folder="../template")
@dashboard.route('/dashboard', methods=["GET","POST"])
def function_name():
    username = session.get('username')
    print(username)
    database = sqlite3.connect("../database/cyber.db")
    cursor = database.cursor()
    cursor.execute("SELECT username,ctf_point,courses_completed,level,ctf_completed FROM security WHERE username=?", (username,))
    fetch = cursor.fetchone()
    return render_template("/home/dashboard.html",cp=fetch[1],cc=fetch[2],level=fetch[3],ctf=fetch[4])