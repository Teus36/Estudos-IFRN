from flask import Flask, render_template, session, request, url_for, redirect
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey'
login_manager = LoginManager()
login_manager.init_app(app)

def get_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@login_manager.user_loader
def load_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    if user:
        return User(user[0], user[1], user[2], user[3])
    return None

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        email = request.form['email']
        matricula = request.form['matricula']
        senha = request.form['senha']

        hashed_senha = generate_password_hash(senha)

        conn = get_connection()
        conn.execute("INSERT INTO users (email, matricula, senha) VALUES (?, ?, ?)", (email, matricula, hashed_senha))
        conn.commit()
        conn.close()
        return redirect(url_for('login'))

    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[3], password):
            login_user(User(user[0], user[1], user[2], user[3]))
            return redirect(url_for('dashboard'))
        
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')  # Adicione um template dashboard.html

if __name__ == '__main__':
    app.run(debug=True)