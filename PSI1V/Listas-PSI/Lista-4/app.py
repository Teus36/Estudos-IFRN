from flask import Flask, request, render_template, session, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = 'chave-secreta' # Necessário para usar sessões

@app.route('/sessao', methods=['GET', 'POST'])
def iniciarSessao():
    if request.method == 'POST':
        session['nome'] = request.form['nome']
        return redirect(url_for('iniciarSessao'))
    nome = session.get('nome')
    return render_template('sessao.html', nome=nome)

@app.route('/limpar_sessao')
def limparSessao():
    session.pop('nome', None)
    return redirect(url_for('limparSessao'))

