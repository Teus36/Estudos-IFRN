from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from sqlalchemy import create_engine

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome:Mapped[str] = mapped_column(nullable= False)
    email:Mapped[str] = mapped_column(nullable=False, unique=True)
    senha:Mapped[str] = mapped_column(nullable=False)

def start_db():
    engine = create_engine("sqlite:///database/database.db")
    session = Session(bind=engine)
    Base.metadata.create_all(bind=engine)

start_db()