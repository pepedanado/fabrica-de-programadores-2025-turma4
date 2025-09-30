import datetime 
from sqlalchemy import *
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, joinedload

DATABASE_URL = "postgresql://postgres:1234@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Usuario(Base):

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    senha_hash = Column(String(255), nullable=False)
    criado_em = Column(DateTime(timezone=True), default=datetime.datetime.now)

    pets = relationship("Pet", back_populates="dono")


class Pet(Base):

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    nome = Column(String(255), nullable=False)
    porte = Column(Text)
    criado_em = Column(DateTime(timezone=True), default=datetime.datetime.now)
    modificado_em = Column(DateTime(timezone=True), default=datetime.datetime.now)

    dono = relationship("Usuario", back_populates="pets")


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso (se não existiam).")
