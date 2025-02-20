from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from database import init_db, register_user, get_user, check_user_password, get_user_by_id

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave-secreta'

# Inicializa o banco de dados
init_db()

# Configuração do Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Classe de usuário para o Flask-Login
class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    user = get_user_by_id(user_id)
    return User(user[0], user[1]) if user else None

# Rota de home (requer login)
@app.route('/')
@login_required
def home():
    return f'Bem-vindo, {current_user.username}! <a href="/logout">Sair</a> | <a href="/{current_user.id}">Meu Perfil</a>'

# Rota de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = check_user_password(username, password)
        if user:
            login_user(User(user[0], user[1]))  # user[0] é ID, user[1] é nome
            return redirect(url_for('home'))
        flash('Login inválido')
    return render_template('login.html')

# Rota de logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Rota de registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if register_user(username, password):
            flash('Conta criada com sucesso! Faça login.')
            return redirect(url_for('login'))
        else:
            flash('Usuário já existe!')
    return render_template('register.html')

# Rota para exibir perfil pelo ID
@app.route('/<int:id>')
@login_required
def profile(id):
    user = get_user_by_id(id)
    if user:
        return render_template('profile.html', user=user)
    return "Usuário não encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)
