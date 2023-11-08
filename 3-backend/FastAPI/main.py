from fastapi import FastAPI
from routers import products, users, auth
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# uvicorn main:app --reload
# Documentacion
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc


@app.get("/")
async def read_root():
    return {'mgs': 'Hola FastAPI'}

app.include_router(products.router)
app.include_router(users.router)
app.include_router(auth.router)
# http://127.0.0.1:8000/static/images/img2.png
app.mount('/static', StaticFiles(directory="static"), name="static")