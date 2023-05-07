from sqlalchemy import Column, Integer, String, DateTime, Date, func
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    surname = Column(String, nullable=False, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, nullable=False)
    bithday = Column(Date, nullable=False)
    information = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), 
                        onupdate=func.now())
