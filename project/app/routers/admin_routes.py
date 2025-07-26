# app/routers/admin_routes.py


from fastapi import APIRouter,HTTPException,Depends,status
from app.schemas.admin_schema import *
from app.schemas.user_schema import ShowUser,CreateUser
from app.database.db import get_db
from sqlalchemy.orm import Session
from app.models.admin_model import Admin
from app.models.user_model import Users
from app.auth.hash import hash_password,verify_password
from app.auth.jwt import create_access_token
from app.auth.dependency import get_current_admin
from typing import List
router = APIRouter(
    prefix="/admin",
    tags=["Site Admin"]
)

@router.post("/")
def create_admin(
    new_admin: AdminCreate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin)  # Required unless first admin
):
    # ✅ Check if any admin already exists
    existing_admin = db.query(Admin).first()

    if existing_admin and not current_admin:
        raise HTTPException(
            status_code=403,
            detail="Only logged-in admins can create new admin accounts."
        )

    # 🔒 Prevent duplicate usernames
    db_admin = db.query(Admin).filter(Admin.username == new_admin.username).first()
    if db_admin:
        raise HTTPException(status_code=400, detail="Username already taken")

    # 🔐 Hash password
    admin_password = hash_password(new_admin.password)

    # 🆕 Create admin
    create_new_admin = Admin(
        name=new_admin.name,
        username=new_admin.username,
        password=admin_password
    )

    db.add(create_new_admin)
    db.commit()
    db.refresh(create_new_admin)

    # 🎫 Token for the new admin
    token = create_access_token({"username": create_new_admin.username})

    admin_data = {
        "id": create_new_admin.id,
        "username": create_new_admin.username,
        "name": create_new_admin.name
    }

    return {
        "message": "Admin created successfully",
        "access_token": token,
        "token_type": "bearer",
        "body": admin_data
    }




@router.post("/login")
def admin_login(
    profile:AdminLogin,
    db:Session = Depends(get_db)
):
    db_admin = db.query(Admin).filter(Admin.username == profile.username).first()

    if not db_admin:
        raise HTTPException(status_code=404,detail="admin not found")
    
    if not verify_password(profile.password,db_admin.password):
        raise HTTPException(status_code=401,detail="Incorrect Admin")
    

    token = create_access_token({
        "username":profile.username
    })

    admin_data = {
        "id": db_admin.id,
        "username": db_admin.username,
        "name": db_admin.name
    }
    return {
        "message":"Login Successfully",
        "access_token":token,
        "token_type":"bearer",
        "body":admin_data
    }



@router.get("/dashboard")
def admin_dashboard(
    current_admin : Admin = Depends(get_current_admin)
):
    return {
        "message": f"Welcome {current_admin.name} to your dashboard.",
        "user": {
            "id": current_admin.id,
            "username": current_admin.username,
            "name":current_admin.name
        }
    }


@router.get("/showUsers",response_model=List[ShowUser])
def show_all_users(
    db:Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
):
    
    all_users  = db.query(Users).all()

    return all_users


@router.post("/new-user",response_model=ShowUser)
def create_new_user(
    new_site_user:CreateUser,
    db:Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
):
    is_user = db.query(Users).filter(Users.username == new_site_user.username).first()

    if is_user:
        raise HTTPException(status_code=400,detail="Username Already Taken")
    
    hashed_pw = hash_password(new_site_user.password)

    user = Users(
        name=new_site_user.name,
        username=new_site_user.username,
        password=hashed_pw 
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@router.delete("/delete-user/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    id:int,
    db:Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
):
    is_user = db.query(Users).filter(Users.id == id).first()

    if not is_user:
        raise HTTPException(status_code=404,detail="User Not Found")
    
    db.delete(is_user)
    db.commit()

    return 