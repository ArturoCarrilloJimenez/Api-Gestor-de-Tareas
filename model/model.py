
from sqlalchemy import Column, VARCHAR, CHAR, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
import uuid

from configs.db import Base

# Clases del modelo SQLAlchemy
class UsersSql(Base) :
    __tablename__ = 'users'

    # Los id son de tipo uuid que se generan automáticamente y por defecto utiliza uuid4
    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True)
    name = Column(VARCHAR(180), default='UserName')
    email = Column(VARCHAR(180), nullable=False, unique=True)
    username = Column(VARCHAR(180), nullable=False, unique=True)
    password = Column(CHAR(60), nullable=False)

    tasks = relationship("TaskSql", back_populates="user")
    
class TaskSql(Base) :
    __tablename__ = 'tareas'

    # Los id son de tipo uuid que se generan automáticamente y por defecto utiliza uuid4
    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True)
    title = Column(VARCHAR(180), nullable=False)
    description = Column(Text)
    completed = Column(Boolean, default=False)
    user_id = Column(CHAR(36), ForeignKey('users.id'), nullable=False)

    user = relationship("UsersSql", back_populates="tasks")
    