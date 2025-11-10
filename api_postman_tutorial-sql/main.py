from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field, Session, create_engine, select

app = FastAPI()

# Modelo da Tabela
class Usuario(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    idade: int

# Criação do Banco
sqlite_url = "sqlite:///database.db"
engine = create_engine(sqlite_url, echo=False)

def criar_tabelas():
    SQLModel.metadata.create_all(engine)

criar_tabelas()

@app.get("/")
def home():
    return {"mensagem": "API com SQLite funcionando!"}

@app.post("/usuarios")
def criar_usuario(nome: str, idade: int):
    with Session(engine) as session:
        usuario = Usuario(nome=nome, idade=idade)
        session.add(usuario)
        session.commit()
        session.refresh(usuario)
        return usuario

@app.get("/usuarios")
def listar_usuarios():
    with Session(engine) as session:
        consulta = select(Usuario)
        resultado = session.exec(consulta).all()
        return resultado

@app.get("/usuarios/{id_usuario}")
def buscar_usuario(id_usuario: int):
    with Session(engine) as session:
        usuario = session.get(Usuario, id_usuario)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return usuario

@app.put("/usuarios/{id_usuario}")
def atualizar_usuario(id_usuario: int, nome: str, idade: int):
    with Session(engine) as session:
        usuario = session.get(Usuario, id_usuario)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        usuario.nome = nome
        usuario.idade = idade
        session.commit()
        return usuario

@app.delete("/usuarios/{id_usuario}")
def deletar_usuario(id_usuario: int):
    with Session(engine) as session:
        usuario = session.get(Usuario, id_usuario)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        session.delete(usuario)
        session.commit()
        return {"mensagem": "Usuário removido com sucesso"}
