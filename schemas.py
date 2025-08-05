from pydantic import BaseModel
from typing import Optional

#for creating a user (input schema)
class UserCreate(BaseModel):
    name: str
    email:str
    password:str
    role:Optional[str]="student"#Default role if not pro

#For sending user data back(output Schema)
class UserOut(BaseModel):
    id:int
    name:str
    email:str
    role:str

    class Config:
        orm_model=True

#For returning JWT tockens(on login)
class Token(BaseModel):
    access_tocken:str
    token_type:str

#For creating a course
class CourseCreate(BaseModel):
    title:str
    description:str
    price:float

#For creating a lesson
class LessonCreate(BaseModel):
    title:str
    video_url:str
