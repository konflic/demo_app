from flask import Blueprint, render_template
from flask import request, url_for, redirect
from .controller import get_data, insert_data, remove_data
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/add', methods=['POST'])
@login_required
def add():
    if request.method == 'POST':
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        address = request.form.get("address")
        insert_data(name, phone, email=email, address=address)
    return redirect(url_for('main.index'))


@main.route('/remove', methods=['POST'])
@login_required
def remove():
    if request.method == 'POST':
        id = request.form.get("id")
        remove_data(id)
    return redirect(url_for('main.index'))


@main.route('/', methods=['GET'])
@login_required
def index():
    data = get_data()
    total_records = len(data)
    return render_template("index.html", data=data, total_records=total_records, login=current_user.login)
