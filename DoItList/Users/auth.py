from datetime import datetime, timedelta

import jwt
from passlib.context import CryptContext

from DoItList.Users.dao import UsersDAO
from DoItList.config import settings

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(raw_password, hashed_password):
    return pwd_context.verify(raw_password, hashed_password)


async def authenticate_user(name: str, password: str):
    user = await UsersDAO.find_one_or_none(name=name)
    if user and verify_password(password, user.hashed_password):
        return user


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)
    return encoded_jwt
