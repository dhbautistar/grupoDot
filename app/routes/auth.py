from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from ..functions_jwt import write_token
from fastapi.responses import JSONResponse

auth_routes = APIRouter()

class User(BaseModel):
    username: str
    email: EmailStr

@auth_routes.post("/login")
def login(user: User):
    print(user.dict())
    if user.username=="Diego Bautista":
        return write_token(user.dict())
    else:
        return JSONResponse(content={"message":"User no found"},status_code=401)
