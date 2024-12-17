from flask import Flask, render_template, url_for, request, redirect
from sqlalchemy import *
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session, Mapped, mapped_column
from models import *

app = Flask(__name__)

engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form['nome']

        if nome:
            user = User(nome=nome)
            session.add(user)
            session.commit()

    users = session.query(User).all()
    return render_template('index.html', users=users)
        
@app.route('/edit/<int:id>', methods=["GET", "POST"])
def edit(id):
    user = session.query(User).get(id)

    if request.method == 'POST':
        user.nome = request.form['nome']
        session.commit()

        return redirect(url_for('index'))

    return render_template('edit.html', user=user)

@app.route('/remove/<int:id>', methods=["GET", "POST"])
def remove(id):
    user = session.query(User).get(id)

    if user:
        session.delete(user)
        session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug=True)




