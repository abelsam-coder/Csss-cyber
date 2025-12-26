from flask import Blueprint,Flask,render_template,request

index = Blueprint('index', __name__,template_folder="../template")

@index.route('/')
def function_name():
    return render_template('/home/index.html')