from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Página inicial'

@app.route('/formulario', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        nome = request.form.get('nome')
        comentario = request.form.get('comentario')
        email = request.form.get('email')
        return f"Obrigado pelo feedback, {nome}!<br> Email:{email} <br> Comentário recebido: {comentario}"
    return "Bem-vindo ao formulário! Por favor, envie seu feedback." + render_template('formulario.html')

