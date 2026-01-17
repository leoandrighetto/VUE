from flask import Flask
from database.db import db
from models import User
from flask_cors import CORS

from routes.auth import auth

app = Flask(__name__)

CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(auth)

if __name__ == "__main__":
    app.run(debug=True)
"""
    No main eu crio a conexão entre o objeto db com meu aplicativo Flask. A única configuração
    exigida é a chave SQLALCHEMY_DATABADE_URI. Que diz para o SQLAlchemy a qual banco de 
    dados se conectar. 

    Após a inicialização do app com o objeto db, eu crio um contexto de aplicação para criar as tabelas

"""
