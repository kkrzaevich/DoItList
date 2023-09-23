from DoItList.Items.models import Items

from DoItList.database import async_session_maker
from sqlalchemy import select, insert, delete, update


class ItemsDAO:
    model = Items

    @classmethod
    async def get_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(Items.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add_item(cls, **data):
        query = insert(cls.model).values(**data).returning(cls.model.id, cls.model.name, cls.model.descriptions,
                                                           cls.model.user_id)
        async with async_session_maker() as session:
            result = await session.execute(query)
            await session.commit()
            return result.mappings().first()

    @classmethod
    async def delete_item(cls, **filer_by):
        async with async_session_maker() as session:
            query = delete(cls.model).filter_by(**filer_by)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update_item(cls, item_id, **data):
        async with async_session_maker() as session:
            query = update(cls.model).filter_by(id=item_id).values(**data)
            await session.execute(query)
            await session.commit()
