from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine  
from .routers import post, user , auth , vote
from .config import settings

#cors policy is used to allow the frontend to access the backend 
#cors policy used to communicate the locathost in the other websites (backend in one website and api from another website)
# models.Base.metadata.create_all(blind=engine)

origins = ["https://www.google.com","https://www.youtube.com","http://localhost:3000","http://localhost:8000"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,         
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router) 

    
# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
#             {"title": "favorite foods", "content": "I like pizza", "id": 2}]

# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i




@app.get("/")
async def root():
    return {"message": "Hello world"}

# @app.get("/sqlalchamy")
# def test_posts(db: Session = Depends(get_db)):
#     #FIRST WE HAVE TO ACCEPT THE DATABASE SEESSION AS A DEPENDENCY (PATH)
#     posts=db.query(model.Post).all()
#     return {"data": posts} 

 