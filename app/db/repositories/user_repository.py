from typing import List, Optional
from app.models.user import User
from sqlalchemy.future import select
from sqlalchemy import delete
from app.db.session import session


class UserRepository:

    async def find_by_user_id(self, user_id: int) -> Optional[User]:
        stmt = select(User).where(User.id == user_id)
        result = await session.execute(stmt)
        return result.scalars().one_or_none()

    async def find_by_manager_email(self, email: str) -> Optional[User]:
        stmt = select(User).where(User.email == email)
        result = await session.execute(stmt)
        return result.scalars().one_or_none()

    async def find_by_user_auth(self, user_auth: str) -> List[User]:
        stmt = select(User).where(User.user_auth == user_auth)
        result = await session.execute(stmt)
        return result.scalars().all()

    async def find_by_user_name(self, user_name: str):
        stmt = select(User).where(User.name == user_name)
        result = await session.execute(stmt)
        return result.scalars().all()

    async def delete_by_user_email(self, user_email: str) -> None:
        stmt = delete(User).where(User.email == user_email)
        await session.execute(stmt)
        await session.commit()

    async def find_all_user(self) -> List[User]:
        stmt = select(User)
        result = await session.execute(stmt)
        return result.scalars().all()

    async def create_user(self, user: User):
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user