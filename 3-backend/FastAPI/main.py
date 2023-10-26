from fastapi import FastAPI

app = FastAPI()

# uvicorn main:app --reload
# Documentacion
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc


@app.get("/")
async def read_root():
    return {'mgs': 'Hola FastAPI'}
