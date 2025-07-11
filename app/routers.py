from fastapi import APIRouter
from .models import User
from .models import Log

router = APIRouter()

@router.post("/create-user")
def create_user(user: User):
    return {
        "message": "User created successfully!",
        "user": {
            "name": user.name,
            "age": user.age,
            "email": user.email
        }
    }

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

