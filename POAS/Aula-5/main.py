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
    SQLModel.metadata.create_all()

@asynccontextmanager
async def lifespan(app: FastAPI):
    get_create_db   
    yield

SessionDep = Annotated[Session, Depends(get_session)]
app = FastAPI(lifespan=lifespan)

@app.get("/alunos")
def alunos(session: SessionDep) -> List[Aluno]:
   alunos = session.exec(select(Aluno)).all()
   return alunos

