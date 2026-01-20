from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from database.db import db
from models import User

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

auth = Blueprint("auth", __name__)


@auth.route("/auth/registrar", methods=["POST"])
def registrar():
    usuario = request.get_json()

    nome = usuario.get("user")
    email = usuario.get("email")
    senha = usuario.get("password")

    dados = ["user", "email", "password"]

    for dado in dados:
        if not usuario.get(dado):
            return jsonify({"Erro": f"{dado} é obrigatório."}), 400

    consulta = User.buscar_usuario(nome, email)

    if consulta:
        return jsonify({"Erro": "Dados já existentes"}), 400

    try:
        password = generate_password_hash(senha)

        user = User(username=nome, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        access_token = create_access_token(identity=user.id)

        return jsonify(
            {"success": "Usuário cadastrado", "access_token": access_token}
        ), 201

    except Exception as e:
        db.session.rollback()
        print(e)
        return jsonify({"Erro": "500"}), 500


@auth.route("/auth/iniciarSessao", methods=["POST"])
def iniciarSessao():
    usuario = request.get_json()

    email = usuario.get("email")
    senha = usuario.get("password")

    dados = ["email", "password"]

    for dado in dados:
        if not usuario.get(dado):
            return jsonify({"erro": f"O {dado} é obrigatório"})

    consulta = User.iniciar_sessao(email, senha)

    if not consulta:
        return jsonify({"Erro": "dados inválidos"}), 400

    try:
        token = create_access_token(identity=usuario.get("id"))
        return jsonify({"success": "Sessão iniciada", "JWT": token})

    except Exception as e:
        db.session.rollback()
        print(e)
        return jsonify({"Erro": "500"}), 500
