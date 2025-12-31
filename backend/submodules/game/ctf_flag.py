# ctf flag input logic API

from flask import Blueprint,render_template,redirect,request,session
import sqlite3

ctf_flag = Blueprint('ctf_flag', __name__)

@ctf_flag.route('/ctf/flag/<id>', methods=["POST","GET"])
def function_name(id):
    username = session.get("username")
    if not username:
        return redirect('/login')
    if request.method == "POST":
        flag_ans = request.form["flag"]
        database = sqlite3.connect("../database/cyber.db")
        cursor = database.cursor()
        cursor.execute("SELECT flag,points FROM ctf_challenges WHERE id = ?",(id,))
        flag = cursor.fetchone()
        if flag and flag[0]:
            if str(flag[0]) == str(flag_ans):
                # cursor.execute("SELECT point FROM users WHERE username = ?",(username,))
                # current_point = int(cursor.fetchone()[0])
                # current_point += flag[0]
                cursor.execute("INSERT INTO security (id,username,ctf_point) VALUES(?,?,?)",(id,username,flag[1]))
                database.commit()
                return render_template('/game/ctf_flag.html',status="success",point=flag[1])
            else:
                return render_template('/game/ctf_flag.html',status="fail",point=flag[1])
        else:
            return render_template('/game/ctf_flag.html',status="error",point=flag[1])
    return render_template('/game/ctf_flag.html')          