from .. import models, schemas  
from fastapi import FastAPI , Response , status , HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func 
from ..database import get_db
from .. import models,oauth2
from typing import Optional, List
from ..utils import my_posts, find_post, find_index_post

router = APIRouter(
    
    prefix = "/posts",
    tags = ['Posts']  
)
  

@router.get("/", response_model=List[schemas.PostOut]) 
def get_posts(
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(oauth2.get_current_user),
    limit: int = 10, 
    skip: int = 0, 
    search: Optional[str] = ""
):
    # Wrap the long query in parentheses to avoid SyntaxError
    posts = (
        db.query(models.Post, func.count(models.Votes.post_id).label("votes"))
        .join(models.Votes, models.Votes.post_id == models.Post.id, isouter=True)
        .group_by(models.Post.id)
        .filter(models.Post.title.contains(search))
        .limit(limit)
        .offset(skip)
        .all()
    )
    
    # print(results)  <-- ERROR: 'results' was undefined
    print(posts)    # Corrected variable name
    
    return posts
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    # 1. Use model.Post (based on your import)
    # 2. use **post.dict() to unpack fields automatically
    # print(current_user.email)
    print(post.dict())
    new_post = models.Post(
        title = post.title,
        content = post.content,
        published = post.published,
        owner_id=current_user.id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

    
@router.get("//latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}

@router.get("/{id}",response_model_exclude=schemas.Post )
def get_post(id: int, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    # SQL query to fetch specific post
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""", str((id),))
    # post = cursor.fetchone()
    
    # post = find_post(id) 
    post_query = db.query(models.Post).filter(models.Post.id == id)
    
    post = post_query.first()
    
    post = db.query(models.Post, func.count(models.Votes.post_id).label("votes")).join(
        models.Votes, models.Votes.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} not found")
    return post                                                       # print(id)   

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    # SQL query to delete post
    
    
    
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    # deleted_post = cursor.fetchone()
    
    # conn.commit() # Important: Save the changes to DB
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    
    # 1. Check if post exists FIRST
    if post_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} does not exist")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail ="not authorzed to perform the requsested action")
    # 2. Delete AFTER checking
    post_query.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/posts/{id}",response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    # SQL query to update post
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", 
    #                (post.title, post.content, post.published, str(id)))
    
    # updated_post = cursor.fetchone()
    
    # conn.commit() # veryy most Important: Save the changes to DB

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    
    # 1. Check if exists
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} does not exist")
        
    if post.owner_id != current_user.id:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail ="not authorzed to perform the requsested action")
    
    # 2. Update (This will now work because Step 1 & 2 fixed the database)
    post_query.update(updated_post.dict(), synchronize_session=False)
    
    db.commit()
    
    return post_query.first()

    # return{"message":"updated post"}
