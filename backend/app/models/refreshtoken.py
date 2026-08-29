from app.core.database import Base
from sqlalchemy import Column,String,Integer,ForeignKey,DateTime,Boolean
from sqlalchemy.orm import relationship
from datetime import datetime


class RefreshToken(Base):
    __tablename__="refreshtokens"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"))
    token=Column(String)
    expired_at=Column(DateTime)
    revoked=Column(Boolean,default=False)
    created_at=Column(DateTime,default=datetime.now())
    
    user=relationship("User",back_populates="refreshtoken")
    
class  Revoked(Base):
    __tablename__="revoked"
    
    id=Column(Integer,primary_key=True)
    token=Column(String)
    expire_at=Column(DateTime)
    revoked_at=Column(DateTime,default=datetime.now)
    