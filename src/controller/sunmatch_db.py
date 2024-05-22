import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from model.sunmatch_db import Instaladores

#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy.ext.declarative import declarative_base

#Base = declarative_base()

# Classe para gerenciar o banco de dados
class GerenciadorBanco:
    def __init__(self, engine, session):
        self.engine = engine #create_engine(f'sqlite:///sunmatch')
        self.session = session #sessionmaker(bind=self.engine)()
        
    def adicionar_registro(self, document, razao_social, telefone, email, estado, cidade):
        registro = Instaladores(
            document=document,
            razao_social=razao_social,
            telefone=telefone,
            email=email,
            estado=estado,
            cidade=cidade
        )
        self.session.add(registro)
        self.session.commit()

    def listar_registros(self):
        return self.session.query(Instaladores).all()


if __name__ == "__main__":
    GerenciadorBanco()
   