from fastapi import APIRouter, Response
from fastapi import HTTPException

from DoItList.Users.auth import get_password_hash, authenticate_user, create_access_token
from DoItList.Users.dao import UsersDAO
from DoItList.Users.schemas import UserAuth

router = APIRouter(prefix='/auth',
                   tags=['Auth and Users'])


@router.post('/register')
async def register_user(user_data: UserAuth):
    existing_user = await UsersDAO.find_one_or_none(name=user_data.name)
    if existing_user:
        raise HTTPException(status_code=409, detail='Пользователь уже существует')
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(name=user_data.name, hashed_password=hashed_password)
    return {'status_code': 200}


@router.post('/login')
async def login_user(response: Response, user_data: UserAuth):
    user = await authenticate_user(user_data.name, user_data.password)
    if not user:
        raise HTTPException(status_code=401, detail='Неверный логин или пароль')
    access_token = create_access_token({'sub': str(user.id)})
    response.set_cookie('todo_access_token', access_token, httponly=True)
    return {'access_token': access_token}
