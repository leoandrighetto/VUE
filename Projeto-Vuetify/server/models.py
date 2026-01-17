from flask import jsonify
from sqlalchemy import Integer, String
from sqlalchemy import select, or_
from sqlalchemy.orm import Mapped, mapped_column
from database.db import db


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)

    @classmethod
    def buscar_usuario(cls, username, email):
        return db.session.execute(
            select(cls).where(or_(cls.username == username, cls.email == email))
        ).scalar_one_or_none()
