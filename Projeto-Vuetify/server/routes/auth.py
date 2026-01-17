from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from database.db import db
from models import User

auth = Blueprint("auth", __name__)


"""
    Esta é o caminho final da rota de registro de novo usuário.
    
    Nesta função eu irei:
      1 validar se todos os dados foram preenchidos no front end.
      2 verificar no banco de dados se existe algum dado repetido que não pode existir.
            2.1 Se um dado estiver repetido, irei retornar um erro para o frontend
            2.2 Se não houver dados repetidos e eles estiverem dentro das regras do banco:
                3 eu criptografo o password
                4 crio o novo objeto no db
"""


@auth.route("/auth/registrar", methods=["POST"])
def registrar():
    # payload = {username, email, password}
    usuario = request.get_json()

    nome = usuario.get("user")
    email = usuario.get("email")
    senha = usuario.get("password")

    dados = ["user", "email", "password"]

    for dado in dados:
        if not usuario.get(dado):
            return jsonify({"Erro": f"{dado} é obrigatório."}), 400

    usuarios = User.query.all()

    for user in usuarios:
        if user.username == nome or user.email == email:
            return jsonify({"Erro": "Dados já existentes"}), 400

    password = generate_password_hash(senha)

    user = User(username=nome, email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"success": "Usuário cadastrado"}), 200
