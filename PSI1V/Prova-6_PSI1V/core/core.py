from flask import Blueprint, render_template
from flask_login import login_required
from database.init_db import *

core = Blueprint('core', 'core', template_folder='templates')
session = Session(bind=engine)

@core.route('/')
def index():
    return render_template('index.html')

@core.route('/users')
@login_required
def users():
    users = session.query(User).all()

    return render_template('core/users.html', users= users)
