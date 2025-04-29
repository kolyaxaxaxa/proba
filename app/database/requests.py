from app.database.models import async_session, User, Category, Item
from sqlalchemy import select, update, delete


# Создаём пользователя
async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()



# Получаем категории из БД
async def get_categories():
    async with async_session() as session:
        return await session.scalar(select(Category))


# Получаем товары
async def get_items_by_category(category_id):
    async with async_session() as session:
        return await session.scalar(select(Item).where(Item.category == category_id))


async def get_item(item_id):
    async with async_session() as session:
        return await session.scalar(select(Item).where(Item.id == item_id))
