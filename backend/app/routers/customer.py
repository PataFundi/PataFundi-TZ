from fastapi import APIRouter,Depends
from app.schemas.customer import CustomerProfileCreate,CustomerProfileUpdate,CustomerProfileResponse
from app.services.customer import CustomerServices
from app.models.user import User
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import get_current_user
router=APIRouter(prefix="/customer/profile",tags=["Customer"])


@router.post("",response_model=CustomerProfileResponse)
def create(data:CustomerProfileCreate,
           current_user:User=Depends(get_current_user),
           db:Session=Depends(get_db)):
    return CustomerServices.customer_create(data,current_user,db)

@router.get("/me",response_model=CustomerProfileResponse)
def get_my(current_user:User=Depends(get_current_user),
           db:Session=Depends(get_db)):
    return CustomerServices.myProfile(current_user,db)

@router.get("/{customt_id}",response_model=CustomerProfileResponse)
def get_my(customer_id:int,current_user:User=Depends(get_current_user),
           db:Session=Depends(get_db)):
    return CustomerServices.get_profile_by_id(customer_id,db)


@router.put("/me",response_model=CustomerProfileResponse)
def update_my(data:CustomerProfileUpdate,
           current_user:User=Depends(get_current_user),
           db:Session=Depends(get_db)):
    return CustomerServices.update_customer(data,current_user,db)




