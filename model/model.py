from pydantic import BaseModel

from sqlalchemy import Column, VARCHAR, CHAR, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
import uuid

from configs.db import Base

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

# Clases del modelo SQLAlchemy
class Users(Base) :
    __tablename__ = 'users'

    # Los id son de tipo uuid que se generan automáticamente y por defecto utiliza uuid4
    id = Column(CHAR(32), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True)
    name = Column(VARCHAR(180), default='UserName')
    email = Column(VARCHAR(180), nullable=False)
    username = Column(VARCHAR(180), nullable=False)
    password = Column(VARCHAR(180), nullable=False)

    tasks = relationship("Task", back_populates="user")

class Task(Base) :
    __tablename__ = 'tareas'

    # Los id son de tipo uuid que se generan automáticamente y por defecto utiliza uuid4
    id = Column(CHAR(32), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True)
    title = Column(VARCHAR(180), nullable=False)
    description = Column(Text)
    completed = Column(Boolean, default=False)
    user_id = Column(CHAR(32), ForeignKey('users.id'), nullable=False)

    user = relationship("Users", back_populates="tasks")
    