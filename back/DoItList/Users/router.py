from fastapi import APIRouter, Response
from fastapi import HTTPException, status

from DoItList.Users.auth import get_password_hash, authenticate_user, create_access_token
from DoItList.Users.dao import UsersDAO
from DoItList.Users.schemas import UserAuth

router = APIRouter(prefix='/auth',
                   tags=['Auth and Users'])


@router.post('/register')
async def register_user(user_data: UserAuth):
    existing_user = await UsersDAO.find_one_or_none(name=user_data.name)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='User already exists')
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(name=user_data.name, hashed_password=hashed_password)
    return {'status_code': 200}


@router.post('/login')
async def login_user(response: Response, user_data: UserAuth):
    user = await authenticate_user(user_data.name, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Wrong username or password')
    access_token = create_access_token({'sub': str(user.id)})
    response.set_cookie('todo_access_token', access_token, httponly=True, path='/', domain='localhost')
    return {'todo_access_token': access_token}


@router.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie('todo_access_token')
    return {'status_code': 200}


@router.post('/all')
async def get_all_users(response: Response):
    return await UsersDAO.find_all()
