from flask import Flask, request, render_template, session, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = 'chave-secreta' # Necessário para gerenciar sessões

usuarios_cadastrados = []


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        nome = request.form['nome']
        # Verificar se o usuário já existe
        for usuario in usuarios_cadastrados:
            if usuario['username'] == username:
                return render_template('cadastro.html', erro='Usuário já cadastrado.')
            # Adicionar novo usuário à lista
            usuarios_cadastrados.append({'username': username, 'password':
            password, 'nome': nome})
            return redirect(url_for('login'))
    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        for usuario in usuarios_cadastrados:
            session['username'] = username
            resposta = make_response(redirect(url_for('dashboard')))
            resposta.set_cookie('username', username, max_age=60*60*24)
            return resposta 
        else:
            return render_template('login.html', erro='Usuário ou senha inválidos.')

    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')   

@app.route('/dashboard')
def dashboard():
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))
    
    return render_template('dashboard.html', username=username)

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)

    resposta = make_response(redirect(url_for('login')))
    resposta.set_cookie('username', '', max_age=0)
    return resposta