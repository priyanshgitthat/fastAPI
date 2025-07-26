from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.schemas.user_schema import CreateUser, ShowUser, LoginUser
from app.models.user_model import Users
from app.auth.hash import hash_password,verify_password
from app.auth.jwt import create_access_token
from app.auth.dependency import get_current_user

from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/user",
    tags=["Site User"]
)
@router.post("/")
def create_new_user(
    new_user: CreateUser,
    db: Session = Depends(get_db)
):
    existing_user = db.query(Users).filter(Users.username == new_user.username).first()
    if existing_user:
        raise HTTPException(status_code=409, detail="Username already taken")
    hashed_pw = hash_password(new_user.password)
    user = Users(
        name=new_user.name,
        username=new_user.username,
        password=hashed_pw 
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    # 🔑 Generate token after successful signup
    token = create_access_token({"username": user.username})

    user_data = {
        "id": user.id,
        "username": user.username,
        "name": user.name
    }

    return {
        "message": "User created and logged in successfully",
        "access_token": token,
        "token_type": "bearer",
        "body": user_data
    }




@router.post("/login")
def user_login(
    profile:LoginUser,
    # profile: OAuth2PasswordRequestForm = Depends(),
    db:Session = Depends(get_db)
):
    db_user = db.query(Users).filter(Users.username == profile.username).first()

    if not db_user:
        raise HTTPException(status_code=404,detail="user not found")
    
    if not verify_password(profile.password,db_user.password):
        raise HTTPException(status_code=401,detail='Incorrect Password')
    token = create_access_token({"username":db_user.username})

    user_data = {
        "id": db_user.id,
        "username": db_user.username,
        "name": db_user.name
    }

    return {
        "message":"Login Successfully",
        "access_token":token,
        "token_type":"bearer",
        "body":user_data
    }

@router.get("/dashboard")
def user_dashboard(
    current_user : Users = Depends(get_current_user)
):
    return {
        "message": f"Welcome {current_user.name} to your dashboard.",
        "user": {
            "id": current_user.id,
            "username": current_user.username,
            "name":current_user.name
        }
    }