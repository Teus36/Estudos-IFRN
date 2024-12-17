from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, session
from werkzeug.security import generate_password_hash, check_password_hash

engine = create_engine('sqlite:///database/database.db')

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id:Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str] = mapped_column(String(100))
    senha:Mapped[str] = mapped_column(String(100)) 

    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = generate_password_hash(senha)

Base.metadata.create_all(engine)   



