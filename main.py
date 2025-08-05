from fastapi import FastAPI
import models
import database
from auth import router as auth_router

models.Base.metadata.create_all(bind=database.engine)

app=FastAPI(title="EdTech Platform")

app.include_router(auth_router,prefix="/auth")

@app.get("/")
def home():
    return {"message":"EdTech API is running"}
