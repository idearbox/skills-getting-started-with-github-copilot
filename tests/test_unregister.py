from src.app import activities


def test_unregister_removes_participant(client):
    response = client.delete("/activities/Chess Club/signup", params={"email": "michael@mergington.edu"})

    assert response.status_code == 200
    assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]


def test_unregister_unknown_activity_returns_404(client):
    response = client.delete("/activities/Nope/signup", params={"email": "a@mergington.edu"})

    assert response.status_code == 404


def test_unregister_not_signed_up_returns_404(client):
    response = client.delete("/activities/Chess Club/signup", params={"email": "ghost@mergington.edu"})

    assert response.status_code == 404


def test_signup_unregister_signup_roundtrip(client):
    params = {"email": "round@mergington.edu"}

    assert client.post("/activities/Chess Club/signup", params=params).status_code == 200
    assert client.delete("/activities/Chess Club/signup", params=params).status_code == 200
    assert client.post("/activities/Chess Club/signup", params=params).status_code == 200
