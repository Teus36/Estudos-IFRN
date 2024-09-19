from flask import Flask, render_template, session, request, url_for, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def get_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/base')
def base():
    return ''

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']

        conexao = get_connection()
        conexao.execute("INSERT INTO tb_user (nome, senha) VALUES (?, ?)", (nome, senha))
        conexao.commit()
        conexao.close()
        return redirect(url_for('index'))

    return render_template('cadastro.html')

