from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_output_routes_to_file():
    routes = sorted((route.path, list(route.methods)) for route in app.routes)
    with open("backend/routes.txt", "w") as f:
        for path, methods in routes:
            f.write(f"{path} {methods}\n")
    # Check that file was written and contains at least the root route
    with open("backend/routes.txt") as f:
        content = f.read()
    assert "/" in content
