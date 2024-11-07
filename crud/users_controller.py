from fastapi import APIRouter, HTTPException, Depends
from starlette import status

from sqlalchemy.orm import Session
from configs.db import get_db
from model.model import Users, UsersPy

routesCrudUser = APIRouter(prefix='/users', tags=['Usuarios'])

@routesCrudUser.get('/', status_code=status.HTTP_200_OK, response_model=list[UsersPy])
def get_tareas(db: Session = Depends(get_db)) -> list[UsersPy] :
    return db.query(Users).all()