from flask import Flask
from flask_login import LoginManager
from src.controller import db
from src.auth import auth as auth_blueprint
from src.main import main as main_blueprint
from src.models import User

login_manager = LoginManager()
app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_storage/users.sqlite'
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

if __name__ == "__main__":
    db.create_all(app=app)
    app.run(host="0.0.0.0", port=os.getenv("PORT", 5000), debug=True)
