from flask import Flask, request, render_template, session, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = 'chave-secreta' # Necessário para usar sessões

@app.route('/', methods=['GET', 'POST'])
def iniciarSessao():
    if request.method == 'POST':
        session['nome'] = request.form['nome']
        return redirect(url_for('iniciarSessao'))
    nome = session.get('nome')
    return render_template('sessao.html', nome=nome)

@app.route('/limpar_sessao')
def limparSessao():
    session.pop('nome', None)
    return redirect(url_for('iniciarSessao'))

@app.route('/cookie', methods=['GET', 'POST'])
def definirCookie():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        resposta = make_response(redirect(url_for('definirCookie')))
        resposta.set_cookie('nome', nome, max_age=60*60*24)
        resposta.set_cookie('idade', idade)
        return resposta
    nome = request.cookies.get('nome')
    idade = request.cookies.get('idade')
    return render_template('cookie.html', nome=nome, idade=idade)