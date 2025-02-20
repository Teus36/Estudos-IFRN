from flask import Flask
from models import db

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'chave-secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()  # Criar tabelas no banco de dados

    return app
