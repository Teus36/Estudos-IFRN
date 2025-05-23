from fastapi import FastAPI, HTTPException
from models import Livro, Usuario, Emprestimo, EmprestimoCreate, DevolucaoCreate
from typing import List
from uuid import uuid4, UUID
from datetime import date

app = FastAPI()

livros: List[Livro] = []
usuarios: List[Usuario] = []
emprestimos: List[Emprestimo] = []

@app.post("/livros/", response_model=Livro)
def criar_livro(livro: Livro):
    livro.id = uuid4()
    livro.liv_disponibilidade = True
    livros.append(livro)
    return livro

@app.get("/livros/", response_model=List[Livro])
def listar_livros():
    return livros

@app.get("/livros/disponiveis/", response_model=List[Livro])
def listar_livros_disponiveis():
    return [livro for livro in livros if livro.liv_disponibilidade]

@app.get("/livros/{titulo}", response_model=Livro)
def buscar_livro_por_titulo(titulo: str):
    for livro in livros:
        if livro.liv_titulo.lower() == titulo.lower():
            return livro
    raise HTTPException(status_code=404, detail="Livro não encontrado")

@app.post("/usuarios/", response_model=Usuario)
def criar_usuario(usuario: Usuario):
    usuario.id = uuid4()
    usuario.usr_livros = []
    usuarios.append(usuario)
    return usuario

@app.post("/emprestimos/", response_model=Emprestimo)
def registrar_emprestimo(dados: EmprestimoCreate):
    livro = next((l for l in livros if l.id == dados.emp_liv_id), None)
    usuario = next((u for u in usuarios if u.id == dados.emp_usr_id), None)

    if not livro or not usuario:
        raise HTTPException(status_code=404, detail="Usuário ou livro não encontrado")
    if not livro.liv_disponibilidade:
        raise HTTPException(status_code=400, detail="Livro indisponível")

    livro.liv_disponibilidade = False
    usuario.usr_livros.append(livro.id)

    emprestimo = Emprestimo(
        id=uuid4(),
        emp_liv_id=livro.id,
        emp_usr_id=usuario.id,
        emp_data_emprestimo=dados.emp_data_emprestimo,
        emp_data_devolucao=None
    )
    emprestimos.append(emprestimo)
    return emprestimo

@app.post("/devolucoes/", response_model=Emprestimo)
def registrar_devolucao(dados: DevolucaoCreate):
    emprestimo = next((e for e in emprestimos if e.emp_liv_id == dados.emp_liv_id and e.emp_usr_id == dados.emp_usr_id and e.emp_data_devolucao is None), None)
    if not emprestimo:
        raise HTTPException(status_code=404, detail="Empréstimo não encontrado ou já devolvido")

    emprestimo.emp_data_devolucao = dados.emp_data_devolucao

    livro = next((l for l in livros if l.id == dados.emp_liv_id), None)
    usuario = next((u for u in usuarios if u.id == dados.emp_usr_id), None)

    if livro:
        livro.liv_disponibilidade = True
    if usuario and livro.id in usuario.usr_livros:
        usuario.usr_livros.remove(livro.id)

    return emprestimo

@app.get("/usuarios/{id_usuario}/livros_emprestados/", response_model=List[Livro])
def listar_livros_emprestados(id_usuario: UUID):
    usuario = next((u for u in usuarios if u.id == id_usuario), None)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return [livro for livro in livros if livro.id in usuario.usr_livros]
