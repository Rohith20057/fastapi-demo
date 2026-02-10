import pytest
from app import schemas 

def test_get_all_posts(authorized_client,test_posts):
    res = authorized_client.get("/posts/")
    
    def validate(post):
        return schemas.PostOut(**post)
    
    posts_map = map(validate, res.json())
    posts_list = list(posts_map)
    print(list(posts_map))
    assert len(res.json()) == len(test_posts)
    
    # posts = res.json()
    # print(res.json())
    assert res.status_code == 200

def test_unauthorized_user_get_all_posts(client, test_post):
    res = client.get("/posts/")
    assert res.status_code == 401

def test_unauthorized_user_get_one_post(client, test_posts):
    res = client.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401
    
    
#fucntin to perform to check that a posts does not exists
def test_get_one_post_not_exist(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/8888")
    assert res.status_code == 404
    
def test_get_one_post(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].id}")
    post = schemas.PostOut(**res.json())
    assert post.Post.id == test_posts[0].id
    assert post.Post.title == test_posts[0].title
    assert post.Post.content == test_posts[0].content
    assert res.status_code == 200
    
@pytest.mark.parametrize("title, content, published", [
    (" awsome new title", "awesome new content", True),
    ("favorite pizza", "i love pepperoni", False),
    ("tallest skyscrapers", "wahoo", True),
])
def test_create_post():
def test_create_posts(authorized_client,test_user,test_posts,published):
    post_data = {
        "title": "New Post",
        "content": "This is a new post",
        "published": True
    }
    res = authorized_client.post("/posts/", json=post_data)
    created_post = schemas.Post(**res.json())
    
    assert created_post.title == post_data['title']
    assert created_post.content == post_data['content']
    assert created_post.published == post_data['published']
    assert res.status_code == 201
    
def test_create_post_default_published_true(authorized_client,test_user):
     res =  authorized_client 
     
     created_post = schemas.post(**res.json())
     
    assert created_post.title == post_data['title']
    assert created_post.content == post_data['content']
    assert created_post.published == post_data['published']
    assert created_post.owner_id == test_user['id']
    assert res.status_code == 201 
    
def create_post_default_published_true(authorized_client,test_user):
    res = authorized_client.post("/posts/", json={"title": "New Post", "content": "This is a new post"})
    created_post = schemas.Post(**res.json())
    assert created_post.title == "New Post"
    assert created_post.content == "This is a new post"
    assert created_post.published == True
    assert created_post.owner_id == test_user['id']
    assert res.status_code == 201

def test_unauthorized_user_create_post(client):
    res = client.post("/posts/", json={"title": "New Post", "content": "This is a new post"})
    assert res.status_code == 401
    
    
def test_unauthorized_user_delete_post(client, test_posts):
    res = client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401 

def test_delete_post_success(authorized_client, test_posts):
    res = authoze 
    res = authorized_client.delete(f"/posts/8888")
    assert res.status_code == 404
    
def test_update_post(authorized_client, test_posts):
    data = {
        "title": "updated title",
        "content": "updated content",
        "id": test_posts[0].id
    }
    res = authorized_client.put(f"/posts/{test_posts[0].id}", json=data)
    updated_post = schemas.Post(**res.json())
    
    assert updated_post.title == data['title']
    assert updated_post.content == data['content']
    assert res.status_code == 200

def test_update_other_user_post(authorized_client, test_posts, test_user):
    data = {
        "title": "updated title",
        "content": "updated content",
        "id": test_posts[4].id
    }
    res = authorized_client.put(f"/posts/{test_posts[3].id}", json=data)
    assert res.status_code == 403   
    
def test_unauthorized_user_update_post(client, test_posts):
    data = {
        "title": "updated title",
        "content": "updated content",
        "id": test_posts[0].id
    }
    res = client.put(f"/posts/{test_posts[0].id}", json=data)
    assert res.status_code == 401
    
def test_delete_post_success(authorized_client, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 204
    assert res.status_code == 204 
    
    