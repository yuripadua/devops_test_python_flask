import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    rv = client.get('/')
    assert rv.data == b'Ola mundo - acaba por favor!!! - BOM DIA JESUS, SEU LINDO!!!!'
