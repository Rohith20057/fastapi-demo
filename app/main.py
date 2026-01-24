from fastapi import FastAPI 
from . import models
from .database import engine  
from .routers import post, user , auth , vote
from .config import settings

print(settings.database_password)


models.Base.metadata.create_all(bind=engine)

app = FastAPI()



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
    return {"message": "Hello baby  how are you"}

# @app.get("/sqlalchamy")
# def test_posts(db: Session = Depends(get_db)):
#     #FIRST WE HAVE TO ACCEPT THE DATABASE SEESSION AS A DEPENDENCY (PATH)
#     posts=db.query(model.Post).all()
#     return {"data": posts} 

 