from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la conexión a la base de datos PostgreSQL
DATABASE_URL = "postgresql://username:password@db:5432/mydatabase"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declaración de la base de datos
Base = declarative_base()

# Modelo de usuario
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String)

app = FastAPI()

# Endpoint "Hola Mundo"
@app.get("/")
async def read_root():
    return {"message": "Hola Mundo"}

# Modelo para la creación de usuarios
class UserCreate(BaseModel):
    username: str
    password: str
    email: str

# Endpoint para guardar usuarios en la base de datos
@app.post("/users/")
async def create_user(user: UserCreate):
    db = SessionLocal()
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return {"message": f"Usuario {user.username} creado correctamente"}
