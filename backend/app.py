# main server file

# modules

from flask import Flask,render_template,request
from submodules.home.index import index
from extension import bcrypt
from submodules.game.ctf_id import ctf_id
from submodules.home.dahsboard import dashboard
from submodules.game.ctf_flag import ctf_flag
from submodules.post.posts import posts
from submodules.activity.activity import activity
from submodules.game.ctf import ctf
from submodules.admin.ctf_install import ctf_install
from submodules.auth.login import login
from submodules.admin.learning_form import learning_form
from submodules.auth.signup import signup
from submodules.post.post_form import post_form



app = Flask(__name__,template_folder="../template",static_folder="../static")
app.secret_key = "csss_cyber_abel"
app.register_blueprint(index)
app.register_blueprint(ctf_flag)
app.register_blueprint(activity)
app.register_blueprint(signup)
app.register_blueprint(learning_form)
app.register_blueprint(login)
app.register_blueprint(ctf_id)
app.register_blueprint(post_form)
app.register_blueprint(ctf)
app.register_blueprint(ctf_install)
app.register_blueprint(posts)
app.register_blueprint(dashboard)
bcrypt.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)