from sqlmodel import SQLModel, create_engine
# from .model import *

sqlite_file_name = 'database.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'

engine = create_engine(sqlite_url, echo=False) # o parâmetro echo mostra informações no terminal

if __name__ == '__main__':
    from model import *
    SQLModel.metadata.create_all(engine)