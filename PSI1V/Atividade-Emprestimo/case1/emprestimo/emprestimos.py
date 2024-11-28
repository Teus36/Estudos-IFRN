from flask import Flask, render_template, url_for, request, Blueprint, redirect
from books.models import Book
from users.models import User
from emprestimo.models import Emprestimo

bp = Blueprint('emprestimo', __name__, url_prefix='/emprestimo', template_folder='templates')

@bp.route('/')
def index():
    return render_template('index.html', emprestimos = Emprestimo.all())

@bp.route('/register', methods=['POST', 'GET'])
def register():

    if request.method == 'POST':
        titulo = request.form['titulo']
        user = request.form['user']
        

        emprestimo = Emprestimo(titulo, user)
        emprestimo.save()
        return redirect(url_for('emprestimo.index'))


    return render_template('register.html', users = User.all())

