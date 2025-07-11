from typing import List, Annotated
from sqlmodel import Session, create_engine, SQLModel, select
from fastapi import FastAPI, Depends
from models import Aluno
from contextlib import asynccontextmanager

url = "sqlite:///banco.db"

connect_args = {"check_same_thread": False}
engine = create_engine(url, connect_args=connect_args)

def get_session():
    with Session(engine) as session:
        yield session 

def get_create_db():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    get_create_db()
    yield

SessionDep = Annotated[Session, Depends(get_session)]
app = FastAPI(lifespan=lifespan)

@app.get("/alunos")
def alunos(session: SessionDep) -> List[Aluno]:
   alunos = session.exec(select(Aluno)).all()
   return alunos

@app.post("/alunos")
def cadastrar(session: SessionDep, aluno: Aluno) -> Aluno:
    session.add(aluno)
    session.commit()
    session.refresh(aluno)
    return aluno

@app.delete("/alunos/{id}")
def deletar(session: SessionDep, id:int) -> str:
    consulta = select(Aluno).where(Aluno.id == id)
    aluno = session.exec(consulta).one()
    session.delete(aluno)
    session.commit()
    return "Aluno deletado com sucesso!!"

@app.put("/alunos/{aluno}")
def atualizar(session: SessionDep, id:int, nome: str) -> Aluno:
    consulta = select(Aluno).where(Aluno.id == id)
    aluno = session.exec(consulta).one()
    aluno.nome = nome
    session.add(aluno)
    session.commit()
    session.refresh(aluno)
    return aluno