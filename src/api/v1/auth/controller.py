from fastapi import APIRouter, HTTPException, Request, Response

from src.lib.exceptions import RegistrationError
from src.api.v1.auth.dtos.registration import RegistrationDTO
from src.apps.user.dto import UserBaseDTO
from src.api.v1.auth.dtos.login import LoginDTO
from src.apps.auth.dependends.service import IAuthService


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/registration", response_model=UserBaseDTO)
async def registration(dto: RegistrationDTO, service: IAuthService, request: Request):
    """
    controller for registration user
    """
    try:
        return await service.registration(dto)
    except (RegistrationError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login")
async def login(response: Response, dto: LoginDTO, service: IAuthService):
    try:
        tokens = await service.login(dto)
        response.set_cookie(
            key="access_token",
            value=tokens.access_token,
            httponly=True,
            samesite="none",
            secure=True,
        )
        response.set_cookie(
            key="refresh_token",
            value=tokens.refresh_token,
            httponly=True,
            samesite="none",
            secure=True,
        )
        return tokens
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
