from fastapi import APIRouter


profile_router = APIRouter(prefix='/profile', tags=['Профиль ользователей'])


from profile import profile_api
