import datetime 
from sqlalchemy import *
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

DATABASE_URL = "postgresql://postgres:1234@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

if __name__ == "__main__":
    Base.metafora.create_all(bind=engine)
    print("Tabelas criadas com sucesso (se não existiam).")

