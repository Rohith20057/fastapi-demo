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


# SQLALCHEMY_DATABASE_URL = "postgressql://postgres:1234@localhost:5432/fastapi_test"
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

# CORRECT (For PostgreSQL)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



# ... imports ...

@pytest.fixture()
def session():
        Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# FIX: Changed scope from "module" to "function" to match the session fixture
@pytest.fixture()
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
    user_data = {"email": "test_user@example.com", "password": "password123"}
    res = client.post("/users/", json=user_data)
    
    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data['password'] # We save the plain password for login tests
    return new_user