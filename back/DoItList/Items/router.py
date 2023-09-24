from fastapi import APIRouter, Depends, HTTPException

from DoItList.Users.models import Users

from DoItList.Users.dependencies import get_current_active_user

from DoItList.Items.schemas import SItems
from pydantic import TypeAdapter
from starlette import status

from DoItList.Items.dao import ItemsDAO

router = APIRouter(prefix='/items',
                   tags=['Items'])


@router.get('')
async def get_all_items(user: Users = Depends(get_current_active_user)) -> list[SItems]:
    return await ItemsDAO.get_all(user_id=user.id)


@router.post('')
async def add_new_item(item_data: SItems, user: Users = Depends(get_current_active_user)):
    item = await ItemsDAO.add_item(name=item_data.name, description=item_data.description, user_id=user.id)
    if not item:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Item not created")
    return item


@router.put('/{item_id}')
async def update_item(item_id: int, new_data: SItems, user: Users = Depends(get_current_active_user)):
    await ItemsDAO.update_item(item_id=item_id, name=new_data.name, description=new_data.description, user_id=user.id)
    return {'message': 'Item updated'}


@router.delete('/{item_id}')
async def remove_item(item_id: int, user: Users = Depends(get_current_active_user)):
    await ItemsDAO.delete_item(id=item_id, user_id=user.id)
    return {'message': 'Item deleted'}
