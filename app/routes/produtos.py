from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.models import models
from app.schemas import produto as produto_schema
from app.models.database import get_db
from app.services.auth import get_current_user
from app.schemas.user import User

# Cria o roteador para as rotas de dados
router = APIRouter()

# --- Rotas para Operadora ---

@router.post("/operadoras/", response_model=produto_schema.Operadora, status_code=status.HTTP_201_CREATED)
def create_operadora(
    operadora: produto_schema.OperadoraCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Cria uma nova operadora (Protegido)."""
    db_operadora = models.Operadora(**operadora.dict())
    db.add(db_operadora)
    db.commit()
    db.refresh(db_operadora)
    return db_operadora

@router.get("/operadoras/", response_model=List[produto_schema.Operadora])
def read_operadoras(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retorna a lista de operadoras."""
    operadoras = db.query(models.Operadora).offset(skip).limit(limit).all()
    return operadoras

# --- Rotas para Segmentacao ---

@router.post("/segmentacoes/", response_model=produto_schema.Segmentacao, status_code=status.HTTP_201_CREATED)
def create_segmentacao(
    segmentacao: produto_schema.SegmentacaoCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Cria uma nova segmentação (Protegido)."""
    db_segmentacao = models.Segmentacao(**segmentacao.dict())
    db.add(db_segmentacao)
    db.commit()
    db.refresh(db_segmentacao)
    return db_segmentacao

@router.get("/segmentacoes/", response_model=List[produto_schema.Segmentacao])
def read_segmentacoes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retorna a lista de segmentações."""
    segmentacoes = db.query(models.Segmentacao).offset(skip).limit(limit).all()
    return segmentacoes

# --- Rotas para Produto ---
@router.post("/produtos/", response_model=produto_schema.Produto, status_code=status.HTTP_201_CREATED)
def create_produto(
    produto: produto_schema.ProdutoCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Cria um novo produto (Protegido)."""
    db_produto = models.Produto(**produto.dict())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)

    # Adiciona os objetos completos de operadora e segmentação para o retorno
    db_produto.operadora = db.query(models.Operadora).get(produto.operadora_id)
    db_produto.segmentacao = db.query(models.Segmentacao).get(produto.segmentacao_id)

    return db_produto