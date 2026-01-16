from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from database.db import db

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


@auth.route("/teste", methods=["POST"])
def teste():
    # payload = {username, email, password}
    usuario = request.get_json()

    nome = usuario.get("user")
    email = usuario.get("email")
    senha = usuario.get("password")

    if not nome or not email or not senha:
        return jsonify({"Erro": "Dados incompletos"}), 400

    else:
        return jsonify(
            {
                "nome": usuario.get("user"),
                "email": usuario.get("email"),
                "senha": usuario.get("password"),
            }
        ), 200
