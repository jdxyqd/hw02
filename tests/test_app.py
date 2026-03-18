import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'欢迎来到我的个人网站' in response.data  # Check for welcome message

def test_about_page(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b'关于我' in response.data  # Check for about section

def test_projects_page(client):
    response = client.get('/projects')
    assert response.status_code == 200
    assert b'我的作品' in response.data  # Check for projects section

def test_contact_page(client):
    response = client.get('/contact')
    assert response.status_code == 200
    assert b'联系我' in response.data  # Check for contact section