from datetime import datetime,timedelta
from app.core.config import settings
import jwt,secrets
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import User
from pwdlib import PasswordHash
from app.models.refreshtoken import Revoked



oauth2_schema=OAuth2PasswordBearer(tokenUrl="/login")


#===========password hashind===========
Password_hash=PasswordHash.recommended()

def hash_password(password):
    hashed=Password_hash.hash(password)
    return hashed

def verify_password(plain_password,hashed_password):
    verified=Password_hash.verify(plain_password,hashed_password)
    return verified

##=============access token========================
def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.now() +timedelta(minutes=settings.EXPIRE_ACCESS_TOKEN)
    to_encode.update({"exp":expire})
    
    token =jwt.encode(to_encode,settings.SECRET_KEY,algorithm=settings.ALGORITHM)
    
    return token


def decode_token(token:str):
    payload=jwt.decode(token,settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid credentials")    
    
    return payload
#==============refresh==========token=========================
def create_refresh_token():
    return secrets.token_urlsafe(64)

#============protect ============routr===============
def get_current_user(token:str=Depends(oauth2_schema),db:Session=Depends(get_db)):
    revoked=db.query(Revoked).filter(Revoked.token==token).first()
    if revoked:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="you logout❌,please login again with your credentials")
    payload=decode_token(token)
    email=payload.get("sub")
    if not email:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="token has no user email")
    user=db.query(User).filter(User.email==email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")
    
    return user
