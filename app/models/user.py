from sqlalchemy import Column, Integer, String, DateTime, Boolean, func, ForeignKey
from app.models.base import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    password = Column(String)
    name = Column(String)
    email = Column(String, unique=True)
    user_auth = Column(String, nullable=True)  # 선생, 학생, 관리자
    is_active = Column(Boolean, default=False)  # 비활성화, 미인증, 인증완료
    email_verified = Column(Boolean, default=False)
    channel = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

