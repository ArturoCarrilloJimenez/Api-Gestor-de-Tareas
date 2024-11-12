from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from sqlalchemy.orm import Session

from model.model import UsersSql
from schemas.schemas import UsersPy

from configs.db import get_db
from utils.hashing import hashing

routesCrudUser = APIRouter(prefix='/users', tags=['Usuarios'])


# Obtengo un usuario en concreto
@routesCrudUser.get('/{id}', status_code=status.HTTP_200_OK, response_model=UsersPy)
async def get_user_by_id(id: str, db: Session = Depends(get_db)) -> UsersPy :
    result = db.query(UsersSql).filter(UsersSql.id == id).first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuario no encontrado')
    return result


# Añado un usuario con las validaciones necesarias
@routesCrudUser.post('/add', status_code=status.HTTP_201_CREATED, response_model=list[UsersPy])
async def add_user(user: UsersPy, db: Session = Depends(get_db)) -> list[UsersPy] :

    # Valido que el email o el nombre de usuario no se haya registrado antes
    emailExist = db.query(UsersSql).filter(UsersSql.email == user.email).first()
    if emailExist :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='El email ya ha sido registrado')
    
    userExist = db.query(UsersSql).filter(UsersSql.username == user.username).first()
    if userExist :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='El nombre de usuario ya ha sido registrado')
    
    # Añado el usuario
    newUsers = UsersSql(name= user.name, email = user.email, username = user.username, password = hashing(user.password))
    db.add(newUsers)
    db.commit()
    db.refresh(newUsers)
    return db.query(UsersSql).all()