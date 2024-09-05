from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
  id: int
  name: str
  surname: str
  url: str
  age: int
  
users_list = [User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=23),
              User(id=2, name="Cris", surname="Dev", url="https://cris.com", age=28),
              User(id=3, name="Ana", surname="Perez", url="https://ana.com", age=25)]

@app.get('/usersjson')
async def usersjson():
  return [{"name":"Alex", "surname":"Lopez","url":"https://moure.dev", "age": 23},
          {"name":"Cris", "surname":"Dev","url":"https://cris.com", "age": 28}, 
          {"name":"Ana", "surname":"Perez","url":"https://ana.dub", "age": 25}]
  

@app.get("/users")
async def users():
  return users_list


@app.get("/user/{id}")
async def user(id: int):
  return search_user(id)
  
  

@app.get("/userquery/")
async def user(id: int):
  return search_user(id)


@app.post("/user/")
async def user(user: User):
  if type(search_user(user.id)) == User:
    return {"error": "El usuario ya existe"}
  else:  #Esto tambien se puede borrar
    users_list.append(user)
    return user
    
@app.put("/user/")
async def user(user: User):
  
  found = False
  
  for index, saved_user in enumerate(users_list):
    if saved_user.id == user.id:
      users_list[index] = user
      found = True
      
  if not found:
    return {"error": "No se ha actualizado el usuario"}
  else:   #esto se puede borrar
    return user
    

@app.delete("/user/{id}")
async def user():
  
  found = False
  
  for index, saved_user in enumerate(users_list):
    if saved_user.id == id:
      del saved_user[index]
      found = True
      
  if not found:
    return {"error": "No se ha eliminado el usuario"}
  

  
def search_user(id: int):
  users = filter(lambda user: user.id == id, users_list)
  try:
    return list(users)[0]
  except:
    return {"error": "No se ha encontrado el usuario"}



  