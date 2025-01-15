from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Base para usar com SQLAlchemy
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Modelo da tabela User
class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(db.String(50), unique=True, nullable=False)

# Criação da tabela ao iniciar o app
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    # Verificar se o usuário já existe antes de adicionar
    if not User.query.filter_by(nome="mudinho").first():
        user = User(nome="mudinho")
        db.session.add(user)
        db.session.commit()

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
