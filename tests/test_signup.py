from src.app import activities


def test_signup_adds_participant(client):
    response = client.post("/activities/Chess Club/signup", params={"email": "new@mergington.edu"})

    assert response.status_code == 200
    assert "new@mergington.edu" in activities["Chess Club"]["participants"]


def test_signup_unknown_activity_returns_404(client):
    response = client.post("/activities/Nope/signup", params={"email": "a@mergington.edu"})

    assert response.status_code == 404


def test_signup_duplicate_returns_400(client):
    response = client.post("/activities/Chess Club/signup", params={"email": "michael@mergington.edu"})

    assert response.status_code == 400
    assert activities["Chess Club"]["participants"].count("michael@mergington.edu") == 1


def test_signup_full_activity_returns_400(client):
    activities["Chess Club"]["max_participants"] = len(activities["Chess Club"]["participants"])

    response = client.post("/activities/Chess Club/signup", params={"email": "late@mergington.edu"})

    assert response.status_code == 400
    assert "late@mergington.edu" not in activities["Chess Club"]["participants"]


def test_signup_missing_email_returns_422(client):
    response = client.post("/activities/Chess Club/signup")

    assert response.status_code == 422
