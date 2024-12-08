from flask import Flask

app = Flask(__name__)



@app.route('/')
def home():
    return "Bem-vindo ao Flask!"

@app.route('/sobre')
def sobre():
    return "Esta página é sobre"

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo ao Flask!"

@app.route('/contato')
def contato():
    return "Esta é a página de contato. <br>Email: mateus@gmail.com <br>Telefone: (84) 99999-9999"
 
