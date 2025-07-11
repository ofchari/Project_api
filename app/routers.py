from fastapi import APIRouter
from .models import Log,User
from .database import user_collection
from .helpers import user_helper

router = APIRouter()

@router.post("/Create_user")
async def Create_user (sign_user : User):
    sign_user_dict = sign_user.dict
    new_sign_user = await user_collection.insert_one(sign_user_dict);
    Create_user = await user_collection.find_one({"_id": new_sign_user.inserted_id})
    return {
        "message" : "Created Data Successfully",
        "User" : user_helper(Create_user)
    }
    

@router.get("/")
async def log ():
        Create_user = await user_collection.find_one();
        return {
            "message" : "Fetched Data Successfully",
            "User" : user_helper(Create_user)
        }
    

