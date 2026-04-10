from database.models.unidade import Unidade


def criar_unidade_service(db, unidade):
    db_unidade = Unidade(
        nome=unidade.nome,
        endereco=unidade.endereco,
        unidade_id=unidade.unidade_id)
    db.add(db_unidade)
    db.commit()
    db.refresh(db_unidade)
    return db_unidade

def listar_unidades_services(db):
    return db.query(Unidade).all()

def listar_unidade_por_id_service(db, unidade_id):
    return db.query(Unidade).filter(Unidade.id == unidade_id).first()

def deletar_unidade_service(db, unidade_id):
    db_unidade = db.query(Unidade).filter(Unidade.id == unidade_id).first()
    if db_unidade:
        db.delete(db_unidade)
        db.commit()
        return True
    return False

def atualizar_unidade_service(db, unidade_id, unidade):
    db_unidade = db.query(Unidade).filter(Unidade.id == unidade_id).first()
    if db_unidade:
        db_unidade.nome = unidade.nome
        db_unidade.endereco = unidade.endereco
        db.commit()
        db.refresh(db_unidade)
        return db_unidade
    return None
