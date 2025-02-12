from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from models import db, User, Post
from database import create_app

app = create_app()

# Configuração do Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Página inicial (Lista todos os usuários)
@app.route('/')
@login_required
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)

# Página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('users'))
        flash('Usuário ou senha inválidos')
    return render_template('login.html')

# Página de logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Página de cadastro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('Usuário já existe!')
            return redirect(url_for('register'))
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Conta criada com sucesso!')
        return redirect(url_for('login'))
    return render_template('register.html')

# Página de perfil do usuário
@app.route('/user/<int:id>')
@login_required
def profile(id):
    user = User.query.get(id)
    if not user:
        return "Usuário não encontrado", 404
    return render_template('profile.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
