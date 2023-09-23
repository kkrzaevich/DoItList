from fastapi import Request, HTTPException, status, Depends
from jose import jwt, JWTError

from DoItList.config import settings

from DoItList.Users.dao import UsersDAO


def get_tokens(request: Request):
    token = request.cookies.get('todo_access_token')
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is not provided",
        )
    return token


async def get_current_active_user(token: str = Depends(get_tokens)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    user_id: str = payload.get('sub')
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    user = await UsersDAO.find_one_or_none(id=int(user_id))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    return user
