from flask import Flask, render_template, request, redirect, url_for
from database.iniciar_db import * 

app = Flask(__name__) 
session = Session(bind=engine)

@app.route('/', methods=['GET', 'POST'])
def cadastrarUser():    
    
    if request.method == 'POST':
        nome = request.form['user']
        senha = request.form['senha']

        if nome and senha: 
            new_user = User(nome=nome, senha=senha)
            session.add(new_user)
            session.commit()
            return redirect(url_for('logarUser'))
        else:
            return render_template('cadastro.html', erro = "Erro!!! Você precisa colocar um nome para continuar")

    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def logarUser():

    if request.method == 'POST':
        nome = request.form['user']
        senha = request.form['senha']
        user = session.query(User).filter_by(nome=nome).first()

        if nome and check_password_hash(user.senha, senha):
            return redirect(url_for('exibirUsers'))
        
        if not nome or not senha:
            return render_template('login.html', erro='ERRO!!! Nome e senha são obrigatórios')

    return render_template('login.html')


@app.route('/users')
def exibirUsers():
    users = session.query(User).all()

    return render_template('users.html', users=users)

@app.route('/remover/<int:id>', methods=['GET', 'POST'])
def removerUser(id):
    user = session.query(User).get(id)

    if user:
        session.delete(user)
        session.commit()

    return redirect(url_for('exibirUsers'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editUser(id):
    user = session.query(User).get(id)

    if request.method == 'POST':
        user.nome = request.form['user']
        session.commit()
        return redirect(url_for('exibirUsers'))
    return render_template('edit.html', user=user)

