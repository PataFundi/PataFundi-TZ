from app.schemas.customer import CustomerProfileCreate,CustomerProfileUpdate
from app.models.customer import Customer
from sqlalchemy.orm import Session
from app.models.user import RoleCheck
from fastapi import HTTPException,status
from datetime import date


class CustomerServices():
    
    @staticmethod
    def calculate_age(dob:date):
        today=date.today()
        if dob.year > today.year:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="date of birth cnnot br in ffuture")
        age=today.year-dob.year-((today.month,today.day)<(dob.month,dob.day))
        return age
        
    @staticmethod
    def customer_create(data:CustomerProfileCreate,current_user,db:Session):
        customer=db.query(Customer).filter(Customer.user_id==current_user.id).first()
        if customer:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="customer already have an account")
    
        if current_user.role != RoleCheck.customer:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="only authorized registerd customer can access")
        customer=Customer(
            full_name=data.full_name,
            gender=data.gender,
            date_of_birth=data.date_of_birth,
            profile_picture=data.profile_picture,
            user_id=current_user.id,
            bio=data.bio,
            age=CustomerServices.calculate_age(data.date_of_birth)
        )
        db.add(customer)
        db.commit()
        db.refresh(customer)
    
        return customer


    @staticmethod
    def myProfile(current_user,db:Session):
        customer=db.query(Customer).filter(Customer.user_id==current_user.id).first()
        return customer
    
    @staticmethod
    def get_profile_by_id(customer_id:int,db:Session):
        customer=db.query(Customer).filter(Customer.id==customer_id).first()
        if not customer:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="customer not found")
        return customer
    
    @staticmethod
    def update_customer(data:CustomerProfileUpdate,current_user,db:Session):
        customer=db.query(Customer).filter(Customer.user_id==current_user.id).first()
        if not customer:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="customer not found")
        if data.full_name:
            customer.full_name=data.full_name
        if data.gender:    
            customer.gender=data.gender
        if data.date_of_birth:    
            customer.date_of_birth=data.date_of_birth
            customer.age=CustomerServices.calculate_age(data.date_of_birth)
        if data.profile_picture:    
            customer.profile_picture=data.profile_picture
        if data.bio:    
            customer.bio=data.bio
    
        db.commit()
        db.refresh(customer)
        return customer