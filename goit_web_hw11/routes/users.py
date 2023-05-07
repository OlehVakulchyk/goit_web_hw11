from typing import Annotated
from pydantic import EmailStr
from fastapi import APIRouter, Depends, HTTPException, Path, status, Query
from sqlalchemy.orm import Session

from goit_web_hw11.database.db import get_db
from goit_web_hw11.schemas import UserResponse, UserModel
from goit_web_hw11.repository import users as repository_users

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[UserResponse])
async def get_users(limit: int = Query(10, le=300), offset: int = 0, db: Session = Depends(get_db)):
    users = await repository_users.get_users(limit, offset, db)
    return users


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int = Path(ge=1), db: Session = Depends(get_db)):
    user = await repository_users.get_user_by_id(user_id, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Not found!")
    return user


@router.get("/search_users/", response_model=list[UserResponse])
async def get_search_users(limit: Annotated[int, Query(le=50)] = 10, 
                            offset: int = 0, 
                            db: Session = Depends(get_db),
                            user_name: Annotated[str | None, 
                                                 Query(description="""_may be empty_ 
                                                 **---to get all users, the following fields must be empty---**""", 
                                                       max_length=20)] = None, 
                            user_surname: Annotated[str | None, 
                                                    Query(description='may be empty', 
                                                          max_length=30)] = None                            
                            ):
    users = await repository_users.get_search_users(limit, 
                                                     offset, 
                                                     db, 
                                                     user_name,
                                                     user_surname
                                                     )
    return users


@router.get("/users_by_email/", response_model=UserResponse)
async def get_users_by_email(user_email: EmailStr,  
                            db: Session = Depends(get_db),
                            ):
    user = await repository_users.get_users_by_email(user_email, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Not found!")
    return user


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(body: UserModel, db: Session = Depends(get_db)):
    user = await repository_users.create(body, db)
    return user


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(body: UserModel, user_id: int = Path(ge=1), 
                      db: Session = Depends(get_db)):
    user = await repository_users.update(user_id, body, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Not found!")
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int = Path(ge=1), db: Session = Depends(get_db)):
    user = await repository_users.remove(user_id, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Not found!")
    return None


@router.get("/bithday_next_days/", 
            response_model=list[UserResponse])
async def get_users_by_bithday(limit: int = Query(10, le=300), 
                               offset: int = 0, 
                               db: Session = Depends(get_db)):
    users = await repository_users.get_users_by_bithday(limit, 
                                                        offset, 
                                                        db)
    return users
