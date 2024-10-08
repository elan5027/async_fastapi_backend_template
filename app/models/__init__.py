# 각 모델 파일을 임포트하여 베이스 메타데이터에 등록
from app.models.user import User

# 모든 모델을 포함한 베이스 모듈
__all__ = [
    "User",
]
