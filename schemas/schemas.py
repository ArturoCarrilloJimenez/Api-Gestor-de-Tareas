from pydantic import BaseModel, Field

# Clases del modelo pydantic
class UsersPy(BaseModel) :
    id : str
    name : str
    email : str
    username : str
    password : str = Field(default=None)

class TaskPy(BaseModel) :
    id : str
    title : str
    description : str
    completed : bool
    user_id : str