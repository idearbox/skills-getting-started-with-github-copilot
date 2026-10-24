def test_get_activities_returns_all_with_expected_fields(client):
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data
    for details in data.values():
        assert {"description", "schedule", "max_participants", "participants"} <= details.keys()


def test_root_redirects_to_static_index(client):
    response = client.get("/", follow_redirects=False)

    assert response.status_code in (302, 307)
    assert response.headers["location"] == "/static/index.html"
