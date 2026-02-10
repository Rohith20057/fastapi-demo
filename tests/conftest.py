from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.main import app
from app import schemas
from app.config import settings
from app.database import get_db
from app.database import Base
from alembic import command
from app import schemas
from app.oauth2 import create_access_token
from app import models



# SQLALCHEMY_DATABASE_URL = "postgressql://postgres:1234@localhost:5432/fastapi_test"
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

# CORRECT (For PostgreSQL)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



# ... imports ...

@pytest.fixture(scope="function")
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# FIX: Changed scope from "module" to "function" to match the session fixture
@pytest.fixture(scope="function")
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
            
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    
    
def test_root(client):
    res = client.get("/")
    print(res.json().get('message'))
    assert res.json().get('message') == 'Hello world'
    assert res.status_code == 200
    
def test_create_user():
    res = client.post( "/users/", json={"email":"hello@123gmail.com", "password":"password123"}
    )
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hello@123gmail.com"
    assert res.status_code == 201

@pytest.fixture
def test_user(client):
    user_data = {"email": "test_user@example.com", "password": "1234"}
    res = client.post("/users/", json=user_data)
    
    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data['password'] # We save the plain password for login tests
    return new_user
@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user['id']})
@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers, 
        "Authorization": f"Bearer {token}"
    }
    return client

@pytest.fixture
def test_posts(test_user, session):
    posts_data = [{
        "title": "first post",
        "content": "first content",
        "owner_id": test_user['id']
    }, {
        "title": "2nd post",
        "content": "2nd content",
        "owner_id": test_user['id']
    }, {
        "title": "3rd post",    
        "content": "3rd content",
        "owner_id": test_user['id']
    }]
    def create_posts_model(post_data):
        return models.Post(**post)
    post_map = map(create_posts_model, posts_data)
    posts = list(post_map)
    
    
    posts = session.query(models.Post).all()
    
    session.add_all(posts)
    session.add_all([models.Post(title=post['title'], content=post['content'], owner_id=post['owner_id']) for post in posts_data])
    session.commit()
    session.query(models.Post).all()
    posts = session.query(models.Post).all()
    return posts