from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, login_user, logout_user
from core.models import User
from database.init_db import *

auth_bp = Blueprint('auth', 'auth', template_folder='templates')
session = Session(bind=engine)

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        # fazer a busca no banco pelo usuário pelo nome
        user = session.query(User).filter_by(nome=nome).first()
        # Aqui você precisa de fato pegar o usuário no banco e logar ele

        if nome and check_password_hash(user.senha, senha):
            login_user(user)
            return redirect(url_for('core.users'))
        
    return render_template('login.html')

@auth_bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        nome = request.form['nome']
        senha = request.form['senha']
        new_user = User(email = email, nome = nome, senha=senha)
        session.add(new_user)
        session.commit()
        return redirect(url_for('auth.login'))
    return render_template('register.html')


@auth_bp.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('core.index'))

