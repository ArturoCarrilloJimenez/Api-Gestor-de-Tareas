from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Cargamos las variables del .env
load_dotenv()

# Leemos las variabes de entorno
DB_HOST = os.getenv('DB_HOST')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')

# Ruta de la base de datos
DATABASE_URL =  f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{DB_HOST}/{MYSQL_DATABASE}"

# Creamos el motor, al comienzo de la ruta de la BD ya especifica que es MySQL
engine = create_engine(DATABASE_URL)

# Luego creamos los parámetros para las sesiones que se crean de dicho motor
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creamos el mapeado ORM
Base = declarative_base()

# Creamos la función para el uso de la sesión
def get_db() :
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()