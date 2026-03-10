# 📝 Task Manager API - Backend Portfolio

Esta é uma API de gerenciamento de tarefas (CRUD) moderna, desenvolvida para demonstrar competências essenciais em **Desenvolvimento Backend com Python**. O projeto foca em escalabilidade, organização de código e persistência de dados real.

---

## 🚀 Tecnologias e Ferramentas

- **Python 3.12+** - Linguagem base
- **FastAPI** - Framework de alta performance, moderno com suporte a Type Hints
- **SQLAlchemy** - ORM para comunicação segura com o banco de dados
- **SQLite** - Banco de dados relacional para armazenamento persistente local
- **Uvicorn** - Servidor ASGI para execução da aplicação
- **Pydantic V2** - Validação rigorosa de dados

---

## 🛠️ Funcionalidades Implementadas

- [x] **Create**: Endpoint `POST /tarefas/` para cadastrar novas tarefas
- [x] **Read**: Endpoint `GET /tarefas/` para listar todas as tarefas salvas
- [x] **Update**: Endpoint `PUT /tarefas/{id}` para alternar o status de conclusão
- [x] **Delete**: Endpoint `DELETE /tarefas/{id}` para remoção definitiva do banco
- [x] **Documentação Automática**: Swagger UI disponível em `/docs`

---

## 📂 Estrutura de Arquivos

```text
.
├── main.py       # Ponto de entrada da API e definição das rotas
├── models.py     # Definição das tabelas do banco de dados (SQLAlchemy)
├── database.py   # Configuração da conexão e sessão do banco
├── .gitignore    # Arquivos ignorados no versionamento (venv, .db, etc.)
└── README.md     # Documentação do projeto
