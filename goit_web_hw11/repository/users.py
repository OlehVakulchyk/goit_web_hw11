from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from goit_web_hw11.database.models import User
from goit_web_hw11.schemas import UserModel

NEXT_DAYS = 7

async def get_users(limit: int, offset: int, db: Session):
    users = db.query(User).limit(limit).offset(offset)
    return users.all()


async def get_user_by_id(user_id: int, db: Session):
    user = db.query(User).filter_by(id=user_id).first()
    return user


async def get_search_users(limit: int, offset: int, 
                            db: Session,
                            user_name: str | None = None, 
                            user_surname: str | None = None
                            ):
    users = db.query(User)
    if user_name:
        users = users.filter_by(name=user_name)
    if user_surname:
        users = users.filter_by(surname=user_surname)
    return users.limit(limit).offset(offset).all()


async def get_users_by_bithday(limit: int, offset: int, db: Session):
    current_datetime = datetime.now().date()
    date_end_bithdays = current_datetime + timedelta(days = NEXT_DAYS)
    users = db.query(User).all()
    users_bithdays = []
    for user in users:
        user_bithday = user.bithday
        bithday_this_year = datetime(
                current_datetime.year, 
                user_bithday.month, 
                user_bithday.day
                ).date()
        if current_datetime < bithday_this_year < date_end_bithdays:
            users_bithdays.append(user)
    return users_bithdays



async def get_users_by_email(user_email: str, db: Session):
    user = db.query(User).filter_by(email=user_email).first()
    return user


async def create(body: UserModel, db: Session):
    user = User(**body.dict())
    print(user) 
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
