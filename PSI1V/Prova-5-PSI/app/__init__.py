from flask import Flask, render_template
from users import users
from books import books
from auth.bp import auth_bp, login_manager

# importar auth_bluprint e login_manager (PROVA)

app = Flask (__name__, template_folder='templates')

# secret key (PROVA)

app.secret_key = 'SEGREDOSECRETO'

#Inicializar app no login_manage (prova)

login_manager.init_app(app)

# registrar blueprint


app.register_blueprint(users.bp)
app.register_blueprint(books.bp)
app.register_blueprint(auth_bp)


@app.route('/')
def index():
    return render_template('layout.html')