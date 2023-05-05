from sqlalchemy.orm import Session

from goit_web_hw11.database.models import User
from goit_web_hw11.schemas import UserModel


async def get_users(limit: int, offset: int, db: Session):
    users = db.query(User).limit(limit).offset(offset).all()
    return users


async def get_user_by_id(user_id: int, db: Session):
    user = db.query(User).filter_by(id=user_id).first()
    return user


async def create(body: UserModel, db: Session):
    user = User(**body.dict())  
    db.add(user)
    db.commit()
    return user


async def update(user_id: int, body: UserModel, db: Session):
    user = await get_user_by_id(user_id, db)
    if user:
        user.name = body.name
        user.surname = body.surname
        user.email = body.email
        user.phone = body.phone
        user.bithday = body.bithday
        user.information = body.information
        db.commit()
    return user


async def remove(user_id: int, db: Session):
    user = await get_user_by_id(user_id, db)
    if user:
        db.delete(user)
        db.commit()
    return user
