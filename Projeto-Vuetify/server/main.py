from flask import Flask
from database.db import db
import models

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)

with app.app_context():
    db.create_all()

"""
    No main eu crio a conexão entre o objeto db com meu aplicativo Flask. A única configuração
    exigida é a chave SQLALCHEMY_DATABADE_URI. Que diz para o SQLAlchemy a qual banco de 
    dados se conectar. 

    Após a inicialização do app com o objeto db, eu crio um contexto de aplicação para criar as tabelas

"""
