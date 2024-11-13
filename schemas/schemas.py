from pydantic import BaseModel, Field
from typing import Optional

# Clases del modelo pydantic
class UsersPy(BaseModel) :
    id : str
    name : Optional[str] = Field(default=None)
    email : Optional[str] = Field(default=None)
    username : str
    password : Optional[str] = Field(default=None)

class TaskPy(BaseModel) :
    id : str
    title : str
    description : str
    completed : bool
    user_id : str