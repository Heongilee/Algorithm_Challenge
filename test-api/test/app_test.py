import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def do_get(client, path):
    response = client.get(path)
    return response.status_code, str(response.data), response.get_json()

def test_simple(client):
    status_code, body, data = do_get(client, '/')
    
    # GET /
    # HTTP Status code : 200
    response = client.get('/')
    assert response.status_code == 200
    assert '"text": "Hello, flask"' in body
    
    data = response.get_json()
    old_count = data['count']

    for i in range(5):
        status_code, body, data = do_get(client, '/')
        new_count = data['count']
        
        assert status_code == 200
        assert new_count == old_count + i + 1