import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Instaladores(Base):
    __tablename__ = 'instaladores'
    id = Column(Integer, primary_key=True)
    document = Column(String, unique=True)
    razao_social = Column(String)
    telefone = Column(String)
    email = Column(String)
    estado = Column(String)
    cidade = Column(String)

    #logo = Column(String, nullable=True)

class StartDb():
    def __init__(self):
        self.engine = create_engine(f'sqlite:///src/model/db/sunmatch')
        self.session = sessionmaker(bind=self.engine)()

    def create_tables(self):
        Base.metadata.create_all(self.engine)
    
if __name__ == "__main__":
    StartDb(),
    Instaladores()


