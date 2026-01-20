from flask import jsonify
from sqlalchemy import Integer, String
from sqlalchemy import select, or_
from sqlalchemy.orm import Mapped, mapped_column
from database.db import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash


class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)

    @classmethod
    def buscar_usuario(cls, username, email):
        return db.session.execute(
            select(cls).where(or_(cls.username == username, cls.email == email))
        ).scalar_one_or_none()

    @classmethod
    def iniciar_sessao(cls, email, password):
        usuario = db.session.execute(
            select(cls).where(cls.email == email)
        ).scalar_one_or_none()

        if not usuario:
            return None

        if check_password_hash(usuario.password, password):
            return usuario

        return None

        """
        checar se o email é válido e existe no banco de dados.
        validar a senha, transformando ela em hash e comparando com o hash cadastrado nos dados do usuário

        """
