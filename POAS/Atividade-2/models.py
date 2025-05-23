from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID
from datetime import date

class Livro(BaseModel):
    id: Optional[UUID] = None
    liv_titulo: str
    liv_autor: str
    liv_ano: int
    liv_disponibilidade: Optional[bool] = True

class Usuario(BaseModel):
    id: Optional[UUID] = None
    usr_nome: str
    usr_livros: List[UUID] = []

class Emprestimo(BaseModel):
    id: UUID
    emp_liv_id: UUID
    emp_usr_id: UUID
    emp_data_emprestimo: date
    emp_data_devolucao: Optional[date] = None

class EmprestimoCreate(BaseModel):
    emp_liv_id: UUID
    emp_usr_id: UUID
    emp_data_emprestimo: date

class DevolucaoCreate(BaseModel):
    emp_liv_id: UUID
    emp_usr_id: UUID
    emp_data_devolucao: date
