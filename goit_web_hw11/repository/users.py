from sqlalchemy.orm import Session

from goit_web_hw11.database.models import User
from goit_web_hw11.schemas import UserModel


async def get_users(limit: int, offset: int, db: Session,
                    user_name: str | None = None):
    users = db.query(User).limit(limit).offset(offset)
    if user_name:
        users = users.filter_by(name=user_name).all()
    else:
       return users.all()


async def get_user_by_id(user_id: int, db: Session):
    user = db.query(User).filter_by(id=user_id).first()
    return user


async def get_users_by_name(limit: int, offset: int, 
                            db: Session,
                            user_name: str | None = None, 
                            user_surname: str | None = None,
                            ):
    users = db.query(User)
    if user_name:
        users = users.filter_by(name=user_name)
    if user_surname:
        users = users.filter_by(surname=user_surname)
    
    return users.limit(limit).offset(offset).all()


async def get_users_by_surname(user_surname: str, 
                               limit: int, offset: int, 
                               db: Session):
    users = db.query(User).filter_by(surname=user_surname).limit(limit).offset(offset).all()
    return users


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
