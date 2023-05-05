from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func, Date
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
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())



# class Owner(Base):
#     __tablename__ = "owners"
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     created_at = Column(DateTime, default=func.now())
#     updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


# class Cat(Base):
#     __tablename__ = "cats"

#     id = Column(Integer, primary_key=True, index=True)
#     nick = Column(String, index=True)
#     age = Column(Integer)
#     vaccinated = Column(Boolean, default=False)
#     description = Column(String)
#     owner_id = Column(Integer, ForeignKey("owners.id"), nullable=True)
#     owner = relationship("Owner", backref="cats")
#     created_at = Column(DateTime, default=func.now())
#     updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
