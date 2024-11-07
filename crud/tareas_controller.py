from fastapi import APIRouter, HTTPException, Depends
from starlette import status

from sqlalchemy.orm import Session
from configs.db import get_db
from model.model import TaskSql
from schemas.schemas import TaskPy

from crud.users_controller import get_user_by_id

routesCrudTask = APIRouter(prefix='/tasks', tags=['Tareas'])

# Obtengo todas las tareas
@routesCrudTask.get('/', status_code=status.HTTP_200_OK, response_model=list[TaskPy])
def get_tareas(db: Session = Depends(get_db)) -> list[TaskPy] :
    return db.query(TaskSql).all()

# Obtengo las tareas de un usuario especifico
@routesCrudTask.get('/{user_id}', status_code=status.HTTP_200_OK, response_model=list[TaskPy])
async def get_tareas(user_id: str, db: Session = Depends(get_db)) -> list[TaskPy] :
    result = db.query(TaskSql).filter(TaskSql.user_id == user_id).all()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuario no encontrado')
    return result

# Añado una tarea
@routesCrudTask.post('/add', status_code=status.HTTP_201_CREATED, response_model=list[TaskPy])
async def add_tarea(task: TaskPy, db: Session = Depends(get_db)) -> list[TaskPy] :

    # Realizar la comprobación del usuario

    newTask = TaskSql(title = task.title, description = task.description, user_id = task.user_id)
    db.add(newTask)
    db.commit()
    db.refresh(newTask)
    return db.query(TaskSql).filter(TaskSql.user_id == task.user_id).all()

# Actualizo una tarea
@routesCrudTask.put('/update/{id}', status_code=status.HTTP_200_OK, response_model=TaskPy)
async def update_tarea(id: str,task: TaskPy, db: Session = Depends(get_db)) -> TaskPy :
    response = db.query(TaskSql).filter(TaskSql.id == id).first()

    if response :

        response.title = task.title
        response.description = task.description
        response.completed = task.completed

        db.commit()
        db.refresh(response)
        return response
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Tarea no encontrado')

# Elimino una tarea
@routesCrudTask.delete('/delete/{id}', status_code=status.HTTP_200_OK, response_model=TaskPy)
async def delete_tarea(id: str, db : Session = Depends(get_db)) -> TaskPy :
    result = db.query(TaskSql).filter(TaskSql.id == id).first()
    if result :
        db.delete(result)
        db.commit()
        return result
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Tarea no encontrado')