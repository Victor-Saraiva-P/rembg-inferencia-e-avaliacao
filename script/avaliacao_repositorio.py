from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config import DB_PATH
from script.classes.avaliacao import Avaliacao
from script.classes.base_orm import Base

engine = create_engine(f"sqlite:///{DB_PATH}", echo=False)
Base.metadata.create_all(engine)

def adicionar_avaliacao(avaliacao: Avaliacao):
    with Session(engine) as s:
        s.add(avaliacao)
        s.commit()
