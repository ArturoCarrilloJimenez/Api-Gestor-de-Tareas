from fastapi import APIRouter, HTTPException, Depends
from starlette import status

from sqlalchemy.orm import Session
from configs.db import get_db
from model.model import Task, TaskPy

routesCrudTask = APIRouter(prefix='/tasks', tags=['Tareas'])

@routesCrudTask.get('/', status_code=status.HTTP_200_OK, response_model=list[TaskPy])
def get_tareas(db: Session = Depends(get_db)) -> list[TaskPy] :
    return db.query(Task).all()