from fastapi import FastAPI
from app.core.config import settings
from app.routers import auth,customer

app=FastAPI(title=settings.APP_NAME)


app.include_router(auth.router)
app.include_router(customer.router)


@app.get("/health")
def checkhealth():
    return{
        "message":"welcome to pata fundi plaform✅✅💰"
    } 