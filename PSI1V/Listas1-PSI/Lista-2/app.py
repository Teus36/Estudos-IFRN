from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/redirecionar')
def redirecionar():
    return redirect(url_for('home'))

@app.route('/sobre')
def sobre():
    return 'Olá, está é a página Sobre'

@app.route('/perfil/<nome>')
def perfil(nome):
    if nome.lower() == "anônimo":
        return redirect(url_for('home'))
    nome_formatado = nome.title()
    return f"Olá, {nome_formatado}! Bem-vindo ao seu perfil."