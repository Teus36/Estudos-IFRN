from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Session, create_engine, select
from models import Pedido
from typing import Annotated
from contextlib import asynccontextmanager

url = "sqlite:///banco.db"
engine = create_engine(url)

def get_session():
    with Session(engine) as session:
        yield session

def create_db():
    SQLModel.metadata.create_all(engine)

SessionDep = Annotated[Session, Depends(get_session)]
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield

app = FastAPI(lifespan=lifespan)
@app.get('/pedidos')
def pedidos(session: SessionDep) -> list[Pedido]:
    pedidos = session.exec(select(Pedido).limit(100)).all()
    return pedidos


