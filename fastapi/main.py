from fastapi import FastAPI
import jwt #pip install pyjwt https://pypi.org/project/PyJWT/
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
 
SECRET_KEY = "cairocoders123456789"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 800
 
dummy_user = {
    "username": "deepdilip",
    "password": "123456ednalan",
}
 
from fastapi.middleware.cors import CORSMiddleware
 
app = FastAPI()
 
app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=["http://localhost:3000"])
 
class Loginclass(BaseModel):
    username: str
    password: str
@app.get("/")
def read_root():
    return {"Hello": "World"}
 
@app.post("/login")
async def login_user(login_item: Loginclass):
    data = jsonable_encoder(login_item)
    if dummy_user['username'] == data['username'] and dummy_user['password'] == data['password']:
        encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
        return {'token': encoded_jwt }
    else:
        return {'message': 'Login failed'}
