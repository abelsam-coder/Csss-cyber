from flask import Flask,render_template,request
from submodules.home.index import index
from extension import bcrypt
from submodules.auth.signup import signup
app = Flask(__name__,template_folder="../template",static_folder="../static")
app.secret_key = "csss_cyber_abel"
app.register_blueprint(index)
app.register_blueprint(signup)
bcrypt.init_app(app)
if __name__ == "__main__":
    app.run(debug=True)