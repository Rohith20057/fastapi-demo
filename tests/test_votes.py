import pytest
from app import models
from app import schemas
import pytest
from fastapi.testclient import TestClient
from tests.conftest import session

@pytest.fixture
def test_vote( test_posts, authorized_client):
    new_vote = models.Vote(post_id=test_posts[3].id, user_id= test_posts[3].owner_id)
    session.add(new_vote)
    session.commit()    


def test_vote_on_post(authorized_client, test_posts):
    res = authorized_client.post("/votes/", json={"post_id": test_posts[0].id, "dir": 1})
    assert res.status_code == 201
    
def test_vote_on_post_twice(authorized_client, test_posts):
    authorized_client.post("/votes/", json={"post_id": test_posts[1].id, "dir": 1})
    res = authorized_client.post("/votes/", json={"post_id": test_posts[1].id, "dir": 1})
    assert res.status_code == 409
    
def test_delete_vote(authorized_client, test_posts):
    authorized_client.post("/votes/", json={"post_id": test_posts[2].id, "dir": 1})
    res = authorized_client.post("/votes/", json={"post_id": test_posts[2].id, "dir": 0})
    assert res.status_code == 201
def test_delete_vote_nonexistent(authorized_client, test_posts):
    res = authorized_client.post("/votes/", json={"post_id": test_posts[0].id, "dir": 0})
    assert res.status_code == 404
def test_vote_nonexistent(authorized_client, test_posts):
    res = authorized_client.post("/votes/", json={"post_id": 8888, "dir": 1})   
    assert res.status_code == 404
    
def test_unauthorized_vote(client, test_posts):
    res = client.post("/votes/", json={"post_id": test_posts[0].id, "dir": 1})
    assert res.status_code == 401