from fastapi import APIRouter, Depends, HTTPException, Header
from requests import Session
from functions_jwt import validate_token, write_token
from fastapi.responses import JSONResponse
from starlette import status

from model.model import UsersSql
from schemas.schemas import UsersPy
from configs.db import get_db
from utils.hashing import verify_password

auth_routes = APIRouter(tags=['Autenticación'])


# Generate jwt 
@auth_routes.post("/login", status_code=status.HTTP_202_ACCEPTED)
def login(user: UsersPy, db: Session = Depends(get_db)):
    result: UsersSql = db.query(UsersSql).filter(UsersSql.username == user.username).first()
    if result and verify_password(user.password,result.password):
        userPy: UsersPy = UsersPy(id = result.id, username = result.username)
        return write_token(userPy.dict())
    else:
        return JSONResponse(content={"detail": "Usuario o contraseña invalida"}, status_code=404)


# Verifico el token creado anteriormente
@auth_routes.post("/verify/token", status_code=status.HTTP_202_ACCEPTED)
def verify_token(Authorization: str = Header(None)):
    if Authorization is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='No has pasado el token')
    token = Authorization.split(" ")[1]
    return validate_token(token, output=True)
    