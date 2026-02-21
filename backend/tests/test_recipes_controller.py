from fastapi.testclient import TestClient
from backend.main import app
from backend.db.db import Base, engine
from fastapi.testclient import TestClient
import pytest

client = TestClient(app)

@pytest.fixture(autouse=True, scope="module")
def setup_db():
    # Create tables before tests
    Base.metadata.create_all(bind=engine)
    yield
    # Drop tables after tests
    Base.metadata.drop_all(bind=engine)

def test_list_recipes_empty():
    response = client.get("/recipes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_recipe_not_found():
    response = client.get("/recipes/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Recipe not found"
