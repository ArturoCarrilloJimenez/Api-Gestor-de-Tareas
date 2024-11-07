from fastapi import FastAPI

from routes.route import routes
from crud.tareas_controller import routesCrudTask
from crud.users_controller import routesCrudUser

import model.model as Models
from configs.db import engine

app = FastAPI()

# Creación del modelo
Models.Base.metadata.create_all(bind=engine)

# Importación de las rutas
app.include_router(routes)
app.include_router(routesCrudTask)
app.include_router(routesCrudUser)

if __name__ == '__main__' :
    import uvicorn
    uvicorn.run(app = 'main:app', host='0.0.0.0', port=8000, reload = True)