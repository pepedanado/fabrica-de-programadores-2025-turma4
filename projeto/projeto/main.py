from tabelas import Usuario, Pet, SessionLocal, joinedload
from sqlalchemy.exc import SQLAlchemyError

def criar_novo_usuario_e_pet(nome_usuario: str, nome_pet: str, email: str, senha_hash: str, porte: str):
    session = SessionLocal()
    try:
        usuario = Usuario(nome=nome_usuario, email=email, senha_hash=senha_hash)
        session.add(usuario)
        session.flush()
        pet = Pet(id_usuario=usuario.id, nome=nome_pet, porte=porte)
        session.add(pet)
        session.commit()
        session.refresh(usuario)
        session.refresh(pet)
        return{"usuario": usuario.nome, "usuario_id": usuario.id, "pet": pet.nome, "pet.id": pet.id}
    except SQLAlchemyError as e:
        session.rollback()
        raise
    finally:
        session.close()

def ler_dados():

    session = SessionLocal()

    users = session.query(Usuario).options(joinedload(Usuario.pets)).all()

    result = []
    for u in users:
        pets = []
        for p in u.pets:
            pets.append({"id": p.id, "nome": p.nome, "porte": p.porte, "criado_em": p.criado_em})
        result.append({"id": u.id, "nome": u.nome, "email": u.email, "criado_em": u.criado_em, "pets": pets})
    return result


def remover_usuario(id_usuario):
    session = SessionLocal()
    usuario_removido = session.query(Usuario).filter(Usuario.id == id_usuario).first()

    if usuario_removido:
        users = session.query(Usuario).options(joinedload(Usuario.pets)).all()

        for u in users:
            for p in u.pets:
                session.delete(p)
                session.commit()
                session.flush()
            session.delete(usuario_removido)
            session.commit()
    
    return print('Usuário de id %s removido com sucessso!' % id_usuario)




