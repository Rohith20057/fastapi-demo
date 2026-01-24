# from passlib.context import CryptContext

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto", bcrypt__ident="2b")

# def hash(password: str):
#     return pwd_context.hash(password)

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)

# --- ADD THIS NEW CODE BELOW ---

my_posts = [{"title": "title of post 1", "content": "content 1", "id": 1}]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i
        
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

def hash(password: str):
    return pwd_context.hash(password)
