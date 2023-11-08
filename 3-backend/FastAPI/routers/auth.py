from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# OAuth2PasswordBearer

oauth2 = OAuth2PasswordBearer(tokenUrl='login')

router = APIRouter(prefix='/login', tags=['auth'])

class User(BaseModel):
    username: str
    fullName: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "kcontreras": {
        "username": "kcontreras",
        "fullName": 'Kendra Contreras',
        "email": 'kendra.contreras@dallase.com',
        "disabled": False,
        "password": "12345"
    },
    "mtanase": {
        "username": "mtanase",
        "fullName": 'Malina Tanase',
        "email": 'tanase123@dallase.com',
        "disabled": True,
        "password": "12345"
    }
}

# Search_user_db
def search_user(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

# search_user
def search_user_2(username: str):
    if username in users_db:
        return User(**users_db[username])
    
async def current_user(token: str = Depends(oauth2)):
    user = search_user_2(token)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Credenciales de auntenticacion invalidas",
            headers={"www-Aunthenticate": "Bearer"}
        )
    
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Usuario Inactivo'
        )
    
    return user
    
@router.post('/login')
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    print('>>>>>', user_db)


    if not user_db:
        raise HTTPException(
            status_code=400, detail="El usuario no es correcto"
        )
    
    user = search_user(form.username)
    print('AQUIII', user)

    if not form.password == user.password:
        raise HTTPException(
            status_code=400, detail="La contrasela no es correcta"
        )
    
    return { "access_token": user.username, "token_type": "bearer" }

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
    
# 4:55:24


