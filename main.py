from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import TarefaModel
from pydantic import BaseModel

# 1. Cria as tabelas no banco de dados (o arquivo test.db aparecerá na pasta)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Portfolio API - Gestor de Tarefas")

# Esquema Pydantic para validação de dados que chegam da API
class TarefaSchema(BaseModel):
    titulo: str
    descricao: str
    concluida: bool = False

    class Config:
        orm_mode = True

# Função para obter uma conexão com o banco em cada requisição
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"status": "Online", "mensagem": "API com Banco de Dados Ativa!"}

# ROTA PARA CRIAR TAREFA (POST)
@app.post("/tarefas/", response_model=TarefaSchema)
def criar_tarefa(tarefa: TarefaSchema, db: Session = Depends(get_db)):
    nova_tarefa = TarefaModel(
        titulo=tarefa.titulo, 
        descricao=tarefa.descricao, 
        concluida=tarefa.concluida
    )
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)
    return nova_tarefa

# ROTA PARA LISTAR TAREFAS (GET)
@app.get("/tarefas/")
def listar_tarefas(db: Session = Depends(get_db)):
    return db.query(TarefaModel).all()

@app.put("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = db.query(TarefaModel).filter(TarefaModel.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    
    tarefa.concluida = not tarefa.concluida # Inverte o status
    db.commit()
    return {"mensagem": "Status da tarefa atualizado!", "tarefa": tarefa}

@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = db.query(TarefaModel).filter(TarefaModel.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    
    db.delete(tarefa)
    db.commit()
    return {"mensagem": "Tarefa removida com sucesso!"}