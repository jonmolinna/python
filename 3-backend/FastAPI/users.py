from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# uvicorn users:app --reload


class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int


users_list = [
    User(id=1, name='Kendra', surname="Contreras", age=27),
    User(id=2, name='Emma', surname="Saez", age=25),
    User(id=3, name='Meryem', surname="Sanchez", age=23),
]


@app.get("/users")
async def users():
    return [
        {"name": 'Kendra', "surname": "Contreras", "age": 27},
        {"name": 'Emma', "surname": "Saez", "age": 25},
        {"name": 'Meryem', "surname": "Sanchez", "age": 23},
    ]


@app.get("/user")
async def user():
    return User(id=1, name="Kendra", surname="Contreras", age=27)


@app.get("/users_class")
async def users_class():
    return users_list


# GET
@app.get("/user/{id}")
async def user(id: int):
    return getUserById(id)


# PATH
# http://127.0.0.1:8000/userquery?id=4
# http://127.0.0.1:8000/userquery?id=4&name=kendra
@app.get("/userquery")
async def user(id: int):
    return getUserById(id)


@app.post("/user")
async def user(user: User):
    if type(getUserById(user.id)) == User:
        return {"error": "El usuario ya existe"}
    else:
        users_list.append(user)
        return user


@app.put("/user")
async def user(user: User):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha actualizado el usuario"}

    return user


@app.delete("/user/{id}")
async def user(id: int):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se ha eliminado el usuario"}


def getUserById(id: int):
    user = filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
