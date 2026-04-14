from fastapi import HTTPException
from database.models.unidade import Unidade


def criar_unidade_service(db, unidade):
    db_unidade = Unidade(
        nome=unidade.nome,
        endereco=unidade.endereco
    )
    db.add(db_unidade)
    db.commit()
    db.refresh(db_unidade)
    return db_unidade


def listar_unidades_service(db):
    return db.query(Unidade).all()


def listar_unidade_por_id_service(db, unidade_id):
    unidade = db.query(Unidade).filter(Unidade.id == unidade_id).first()

    if not unidade:
        raise HTTPException(status_code=404, detail="Unidade não encontrada")

    return unidade


def deletar_unidade_service(db, unidade_id):
    unidade = db.query(Unidade).filter(Unidade.id == unidade_id).first()

    if not unidade:
        raise HTTPException(status_code=404, detail="Unidade não encontrada")

    db.delete(unidade)
    db.commit()


def atualizar_unidade_service(db, unidade_id, unidade):
    db_unidade = db.query(Unidade).filter(Unidade.id == unidade_id).first()

    if not db_unidade:
        raise HTTPException(status_code=404, detail="Unidade não encontrada")

    dados = unidade.model_dump(exclude_unset=True)

    for campo, valor in dados.items():
        setattr(db_unidade, campo, valor)

    db.commit()
    db.refresh(db_unidade)
    return db_unidade