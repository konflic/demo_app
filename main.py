from flask import Blueprint, render_template
from controller import get_data
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
@login_required
def index():
    data = get_data()
    total_records = len(data)
    return render_template("index.html", data=data, total_records=total_records, login=current_user.login)
