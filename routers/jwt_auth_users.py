from fastapi import FastAPI, Depends, HTTPException, status   # type: ignore
from pydantic import BaseModel  # type: ignore
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm # type: ignore

app = FastAPI()

# creamos instancia de nuestro sistema de autenticacion
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
  username: str
  full_name: str
  email: str
  disabled: bool
  
class UserDB(User):
  password: str
  
users_db = {
  "halexdev": {
    "username": "halexdev",
    "full_name": "Halex Calcina",
    "email": "halex10@gmail.com",
    "disabled": False,
    "password": "123456"
  },
  "halexdev2": {
    "username": "halexdev2",
    "full_name": "Halex Lopez",
    "email": "halex@gmail.com",
    "disabled": True,
    "password": "654321"
  }
}