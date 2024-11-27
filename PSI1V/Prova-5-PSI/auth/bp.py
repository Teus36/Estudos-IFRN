from flask import render_template, url_for, request, Blueprint, redirect
from flask_login import LoginManager, login_user, login_required, logout_user
from users.models import User


auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth', template_folder='templates')
login_manager = LoginManager()
login_manager.login_view = 'auth_bp.login'


@login_manager.user_loader
def load_user(user_id):
    return User.find(id=user_id)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        nome = request.form['nome']
        
        user = User.find(email=email)
        if user:
            login_user(user)
            return redirect(url_for('users.index'))
        
    return render_template('login.html')

@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.register'))