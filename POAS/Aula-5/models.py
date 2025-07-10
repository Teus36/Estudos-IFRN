from sqlmodel import SQLModel, Field

class Aluno(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nome: str 
    matricula: str 