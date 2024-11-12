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
@auth_routes.post("/login")
def login(user: UsersPy, db: Session = Depends(get_db)):
    result = db.query(UsersSql).filter(UsersSql.username == user.username).first()
    print(result)
    if result and verify_password(user.password,result.password):
        return write_token(user.dict()) # TODO exportar el usuario de la base de datos no del que introduce
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=404)


# Verifico el token creado anteriormente
@auth_routes.post("/verify/token")
def verify_token(Authorization: str = Header(None)):
    if Authorization is None:
        raise HTTPException(status_code=401, detail='No has pasado el token')
    token = Authorization.split(" ")[1]
    return validate_token(token, output=True)
    