## **README - Projeto 2 (CRUD com SQLite + SQLModel)**

```md
# API de Usuários - CRUD com SQLite (FastAPI + SQLModel)

Versão aprimorada da API básica, agora utilizando banco de dados SQLite para persistência.  
Excelente para aprender rotas REST e testar chamadas no Postman.

## Tecnologias
- Python
- FastAPI
- Uvicorn
- SQLModel (SQLAlchemy + Pydantic simplificado)
- SQLite

## Instalação

Instale as dependências:

```bash
pip install fastapi uvicorn sqlmodel
Executando o Servidor
bash
Copiar código
uvicorn main:app --reload
A API ficará disponível em:

cpp
Copiar código
http://127.0.0.1:8000
Documentação interativa:

arduino
Copiar código
http://127.0.0.1:8000/docs
Banco de Dados
O arquivo database.db será criado automaticamente na primeira operação de escrita (POST).

Rotas para Testar no Postman
Método	Rota	Descrição
GET	/	Testa se a API está ativa
POST	/usuarios?nome=NOME&idade=IDADE	Cria um usuário
GET	/usuarios	Lista todos os usuários
GET	/usuarios/{id}	Busca usuário por ID
PUT	/usuarios/{id}?nome=NOME&idade=IDADE	Atualiza um usuário
DELETE	/usuarios/{id}	Remove um usuário

Exemplo de Criação de Usuário
nginx
Copiar código
POST http://127.0.0.1:8000/usuarios?nome=Maria&idade=30
Retorno esperado:

json
Copiar código
{
  "id": 1,
  "nome": "Maria",
  "idade": 30
}
