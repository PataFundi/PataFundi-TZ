from app.core.database import Base
from sqlalchemy import Column,String,Integer,DateTime,ForeignKey,Text,Date
from datetime import datetime
from sqlalchemy.orm import relationship

class Customer(Base):
    __tablename__="customers"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"))
    full_name=Column(String,nullable=False)
    gender=Column(String,nullable=True)
    date_of_birth=Column(Date,nullable=True)
    age=Column(Integer,nullable=True)
    profile_picture=Column(String,nullable=True)
    bio=Column(Text,nullable=True)
    created_at=Column(DateTime,default=datetime.now)
    updated_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    
    user=relationship("User",back_populates="customer")
    