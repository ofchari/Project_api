from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

         
    #   Login User Model 
class Log(BaseModel):
    name: str
    password: str