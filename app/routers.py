from fastapi import APIRouter
from .models import Log,User
from .database import user_collection
from .helpers import user_helper

router = APIRouter()



@router.post("/auth_login")
def auth_login(log : Log):
    return {
        "data" : "Created Successfully",
        "log" : {
            "username" : log.name,
            "password" : log.password
        }
    }


@router.get("/")
def login():
    return {"message": "Hi FastAPI Dev"}


@router.get("/login_data")
def login():
    return {
        "message": "fetched Data Successfully",
        "users": [
            {"name": "HK", "password": "123"},
            {"name": "Hari", "password": "456"}
        ]
    }

