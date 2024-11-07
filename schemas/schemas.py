from pydantic import BaseModel

# Clases del modelo pydantic
class UsersPy(BaseModel) :
    id : str
    name : str
    email : str
    username : str
    password : str

class TaskPy(BaseModel) :
    id : str
    title : str
    description : str
    completed : bool
    user_id : str