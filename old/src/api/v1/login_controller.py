from fastapi import APIRouter, HTTPException

from old.src.domain.auth.token_dto import Token
from src.lib import LoginError
from old.src.app.dependencies.services import ILoginService

router = APIRouter(prefix="/login", tags=["login"])


@router.post("/", response_model=Token)
async def login_user(service: ILoginService, email: str, password: str):
    try:
        return await service.check(email, password)
    except LoginError as e:
        raise HTTPException(status_code=400, detail=str(e))
