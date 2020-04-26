from flask import Flask
from flask import request, url_for, redirect
from flask_login import LoginManager
from controller import crate_table, insert_data, remove_data, db
from auth import auth as auth_blueprint
from main import main as main_blueprint
from models import User
from flask_login import login_required

login_manager = LoginManager()
app = Flask(__name__)

app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite'
db.init_app(app)

# Set the default login page
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table,
    # use it in the query for the user
    return User.query.get(int(user_id))


# For docker run --rm -p 80:80 -v $(pwd):/app {IMAGE_NAME}
@app.route('/add', methods=['POST'])
@login_required
def add():
    if request.method == 'POST':
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        address = request.form.get("address")
        insert_data(name, phone, email=email, address=address)
    return redirect(url_for('main.index'))


@app.route('/remove', methods=['POST'])
@login_required
def remove():
    if request.method == 'POST':
        id = request.form.get("id")
        remove_data(id)
    return redirect(url_for('main.index'))


if __name__ == "__main__":
    crate_table()
    db.create_all(app=app)
    app.run(debug=True, host="0.0.0.0", port="80")
