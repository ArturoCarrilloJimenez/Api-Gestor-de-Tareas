from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.route import routes
from crud.tareas_controller import routesCrudTask
from crud.users_controller import routesCrudUser

import model.model as Models
from configs.db import engine

app = FastAPI()

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
app.include_router(routes)
app.include_router(routesCrudTask)
app.include_router(routesCrudUser)

if __name__ == '__main__' :
    import uvicorn
    uvicorn.run(app = 'main:app', host='0.0.0.0', port=8000, reload = True)