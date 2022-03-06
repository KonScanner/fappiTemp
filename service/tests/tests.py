from starlette.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_endpoint():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {
        "message": "Hello World",
        "usage": "Call /api/movie/{title} to get movie data",
    }


# def test_users_endpoint():
#     resp = client.get("/users/1")
#     assert resp.status_code == 200
#     assert resp.json() == {"user_id": 1}


# def test_create_item_endpoint():
#     resp = client.post("/items/", json={"name": "test", "price": 1.0})
#     assert resp.status_code == 200
#     assert resp.json() == {"item_name": "test", "item_price": 1.0}


# def test_sleep_slow_endpoint():
#     resp = client.get("/sleep_slow_1")
#     assert resp.status_code == 200
#     assert resp.json() == {"seconds": 1}


# def test_sleep_fast_endpoint():
#     resp = client.get("/sleep_fast_1")
#     assert resp.status_code == 200
#     assert resp.json() == {"seconds": 1}


# def test_correct_item():
#     resp = client.post("/items/", json={"name": "test", "price": -1.0})
#     resp2 = client.post("/items/", json={"name": "test", "price": 1.0})
#     assert resp.status_code == 422
#     assert resp2.status_code == 200
