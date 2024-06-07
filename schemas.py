from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]

    class Config:
        orm_mode=True
        schema_extra={
            'example':{
                "username":"johndoe",
                "email":"johndoe@gmail.com",
                "password":"password",
                "is_staff":False,
                "is_active":True
            }
        }


class Settings(BaseModel):
    authjwt_secret_key:str='23641e674692c5877fa1f5ffe5fbdc2db6076c31ddd31a82fee2e48991a41525'

class LoginModel(BaseModel):
    username:str
    password:str

