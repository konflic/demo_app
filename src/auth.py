from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from .controller import db, create_table
from uuid import uuid1

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET'])
def login():
    if not current_user.is_authenticated:
        return render_template("login.html")
    else:
        return redirect(url_for('main.index'))


@auth.route('/login', methods=['POST'])
def login_post():
    login = request.form.get('login')
    password = request.form.get('password')

    user = User.query.filter_by(login=login).first()

    if not user or not check_password_hash(user.password, password):
        return redirect(url_for('auth.login'))

    login_user(user, remember=True)
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET'])
def register():
    if not current_user.is_authenticated:
        return render_template("register.html")
    else:
        return redirect(url_for('main.index'))


@auth.route('/register', methods=['POST'])
def register_post():
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if password != password2:
        return "Password not match!"

    user = User.query.filter_by(login=login).first()

    if user:
        flash("Registration error!")
        return redirect(url_for('auth.register'))

    contacts_table = login + "_" + str(uuid1()).replace("-", "_")

    new_user = User(
        login=login,
        password=generate_password_hash(password, method='sha256'),
        contacts=contacts_table
    )

    db.session.add(new_user)
    create_table(contacts_table)
    db.session.commit()

    flash("New user registered!")
    return redirect(url_for('auth.register'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
