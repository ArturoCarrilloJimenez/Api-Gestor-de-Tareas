from fastapi import FastAPI

from routes.route import routes

import model.model as Models
from configs.db import engine

app = FastAPI()

Models.Base.metadata.create_all(bind=engine)

app.include_router(routes)

if __name__ == '__main__' :
    import uvicorn
    uvicorn.run(app = 'main:app', host='0.0.0.0', port=8000, reload = True)