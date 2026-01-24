from pydantic import BaseModel, EmailStr, conint, ConfigDict
from typing import Optional
from datetime import datetime

class Post(BaseModel):
    title: str
    content: str
    published: bool 
    rating: Optional[int] = None
    
    
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    # created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class post(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime
    rating: Optional[int] = None
    owner_id: int
    owner: UserOut
    

    model_config = ConfigDict(from_attributes=True)
        
class PostOut(PostBase):
    posts: Post
    votes: int
    
    model_config = ConfigDict(from_attributes=True)
        
class UserCreate(BaseModel):
    email: EmailStr
    password: str 


class UserLogin(BaseModel):
    email:EmailStr
    password:str
    
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

def vote(BaseModel):
    post_id: int
    dir:conint(le=1)