from pydantic import BaseModel, EmailStr, conint, ConfigDict
from datetime import datetime
from typing import Optional




class PostBase(BaseModel):
    title:str
    content:str
    published: bool = True



class PostCreate(PostBase):      #user sending data to us
    pass



class UserOut(BaseModel):
    id: int
    email: EmailStr 
    created_at: datetime

    class Config:
        orm_mode = True






class Post(PostBase):     #we sending data to user(RESPONSE)
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    
    class Config:
        orm_mode = True   




class PostOut(BaseModel):
    Post: Post
    votes: int
    model_config = ConfigDict(from_attributes=True)            
    






class UserCreate(BaseModel):
    email: EmailStr
    password: str





class UserLogin(BaseModel):
    email: EmailStr
    password: str




class Token(BaseModel):
    access_token: str
    token_type: str      



class TokenData(BaseModel):
    id: Optional[str] = None         




class Vote(BaseModel):
    post_id: int
    dir: int = conint(le = 1)
