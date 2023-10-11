from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Endpoint "Hola Mundo"
@app.get("/")
async def read_root():
    return {"message": "Hola Mundo"}

# Modelo para la creación de usuarios
class User(BaseModel):
    username: str
    password: str
    email: str

users = []

# Endpoint para guardar usuarios en la base de datos
@app.post("/users/")
async def create_user(user: User):
    users.append(user)
    return {"message": f"Usuario {user.username} creado correctamente"}

# Endpoint para regresar la lista de usuarios
@app.get("/users/")
async def get_users():
    return {"users":users}
