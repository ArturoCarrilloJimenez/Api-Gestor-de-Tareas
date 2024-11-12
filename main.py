from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.crud.tareas_controller import routesCrudTask
from routes.crud.users_controller import routesCrudUser
from routes.auth import auth_routes

import model.model as Models
from configs.db import engine

app = FastAPI(title='Api Gestor de Tareas', version='1.0')

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:4200",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Creación del modelo
Models.Base.metadata.create_all(bind=engine)

# Importación de las rutas
app.include_router(routesCrudTask)
app.include_router(routesCrudUser)
app.include_router(auth_routes)

if __name__ == '__main__' :
    import uvicorn
    uvicorn.run(app = 'main:app', host='0.0.0.0', port=8000, reload = True)