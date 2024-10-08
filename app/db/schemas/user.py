from typing import Optional
from datetime import datetime
from app.models.user import User, ApplicationForm
from pydantic.dataclasses import dataclass


@dataclass
class UserCreateReq:
    email: str
    name: str
    password: str
    channel: str
    # auth: str #관리자, 학생, 선생


@dataclass
class UserLoginReq:
    email: str
    password: str


@dataclass
class UserResp:
    id: int
    name: str
    email: str
    user_auth: str
    is_active: bool
    channel: str
    email_verified: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

    @classmethod
    def from_dto(cls, admin: User) -> "UserResp":
        return UserResp(
            id=admin.id,
            created_at=admin.created_at,
            updated_at=admin.updated_at,
            name=admin.name,
            email=admin.email,
            user_auth=admin.user_auth,
            is_active=admin.is_active,
            email_verified=admin.email_verified,
            channel=admin.channel,
        )
