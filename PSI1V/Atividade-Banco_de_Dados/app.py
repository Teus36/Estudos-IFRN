from flask import Flask, request, render_template, url_for, \
    session, redirect
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'superdificil'

def get_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dash():    
    if 'user' in session:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'user' in session:
        return redirect(url_for('dash'))

    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']

        # Verificar se o usuário existe no banco de dados
        conexao = get_connection()
        cursor = conexao.execute("SELECT * FROM users WHERE nome = ? AND senha = ?", (nome, senha))
        user = cursor.fetchone()
        conexao.close()

        if user:  # Se encontrar o usuário
            session['user'] = nome
            return redirect(url_for('dash'))
        else:
            return "Usuario inexistente ou senha incorreta"

    return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():

    ## esse bloco tanto para register quanto para login
    if 'user' in session:
        return redirect(url_for('dash'))

    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']

        conexao = get_connection
        user = conexao.execute("SELECT * FROM users WHERE email= ?" (nome, )).fetchone()

        # regsitrar no banco 
        if user:
            conexao.close()
            return "O usuário já está cadastrado"
        else:
            conexao.execute("INSERT INTO users (email, senha) VALUES(?, ?)", (nome, senha))
            conexao.commit()
            conexao.close()
            return redirect(url_for('dash'))

    return render_template('register.html')

@app.route('/logout', methods=['POST', 'GET'])
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))