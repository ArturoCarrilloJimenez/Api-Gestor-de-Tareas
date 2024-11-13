from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from sqlalchemy.orm import Session

from middlewares.verify_token_route import VerifyTokenRoute
from model.model import TaskSql
from schemas.schemas import TaskPy

from configs.db import get_db
from routes.crud.users_controller import get_user_by_id

routesCrudTask = APIRouter(prefix='/tasks', tags=['Tareas'], route_class=VerifyTokenRoute)


# Obtengo las tareas de un usuario especifico
@routesCrudTask.get('/{user_id}', status_code=status.HTTP_200_OK, response_model=list[TaskPy])
async def get_tareas(user_id: str, db: Session = Depends(get_db)) -> list[TaskPy] :
    result = db.query(TaskSql).filter(TaskSql.user_id == user_id).all()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuario no encontrado')
    return result


# Obtengo una tarea de un usuario especifico
@routesCrudTask.get('/{user_id}/{task_id}', status_code=status.HTTP_200_OK, response_model=TaskPy)
async def get_tarea_by_id(task_id: str, user_id: str, db: Session = Depends(get_db)) -> TaskPy :
    result = db.query(TaskSql).filter(TaskSql.user_id == user_id, TaskSql.id == task_id).first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Tarea no encontrado')
    return result


# Añado una tarea
@routesCrudTask.post('/add', status_code=status.HTTP_201_CREATED, response_model=list[TaskPy])
async def add_tarea(task: TaskPy, db: Session = Depends(get_db)) -> list[TaskPy] :

    user_id: str = task.user_id
    await get_user_by_id(user_id, db)

    newTask = TaskSql(title = task.title, description = task.description, user_id = task.user_id)
    db.add(newTask)
    db.commit()
    db.refresh(newTask)
    return db.query(TaskSql).filter(TaskSql.user_id == task.user_id).all()


# Actualizo una tarea
@routesCrudTask.put('/update/{user_id}/{task_id}', status_code=status.HTTP_200_OK, response_model=TaskPy)
async def update_tarea(task_id: str, user_id: str, task: TaskPy, db: Session = Depends(get_db)) -> TaskPy :
    response = db.query(TaskSql).filter(TaskSql.user_id == user_id, TaskSql.id == task_id).first()

    if response :

        response.title = task.title
        response.description = task.description
        response.completed = task.completed

        db.commit()
        db.refresh(response)
        return response
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Tarea no encontrado')


# Elimino una tarea
@routesCrudTask.delete('/delete/{user_id}/{task_id}', status_code=status.HTTP_200_OK, response_model=TaskPy)
async def delete_tarea(task_id: str, user_id: str, db : Session = Depends(get_db)) -> TaskPy :
    result = db.query(TaskSql).filter(TaskSql.user_id == user_id, TaskSql.id == task_id).first()
    if result :
        db.delete(result)
        db.commit()
        return result
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Tarea no encontrado')