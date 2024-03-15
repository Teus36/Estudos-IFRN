from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def index():
    return "<h1>Olá mundo</h1>"

@app.route('/dashboard')

def dashboard():
    dados = {
        'nome': 'Mateus Batista',
        'cidade': 'Caicó',
        'turma': 'Info 1V'
    }
    return render_template('/dashboard.html', dados=dados)

@app.route('/profile')

def profile():
    nome = request.args.get('nome')
    
    if nome == None:
        nome = 'Emitibi'
    
    return render_template('/profile.html', nome=nome)