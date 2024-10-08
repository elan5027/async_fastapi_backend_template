from fastapi import APIRouter
from app.api.v1 import user, aws

router = APIRouter()

router.include_router(user.router, tags=["User"], prefix="/user")
router.include_router(aws.router, tags=["AWS"], prefix="/aws")
