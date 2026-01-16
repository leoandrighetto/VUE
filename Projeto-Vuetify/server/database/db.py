from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

"""
    primeiro cria-se o OBJETO db utilizando o construtor SQLAlchemy
    passando uma subclasse de DeclarativeBase para o construtor.

    Uma vez construido, o objeto db me dá acesso à classe db.Model para definir as tabelas
    do meu banco de dados e a sessão db para executar requisições.
"""