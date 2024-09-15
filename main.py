from fastapi import FastAPI # type: ignore
from routers import products, users
from fastapi.staticfiles import StaticFiles # type: ignore

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
async def root():
  return "Hola FastAPI"

@app.get('/url')
async def url():
  return {"url_curso":"https::/mouredev.com/python"}