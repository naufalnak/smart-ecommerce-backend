def test_register(client):
    response = client.post(
        "/auth/register",
        json={
            "email": "pytestuser@mail.com",
            "password": "123456"
        }
    )

    # kalau email sudah pernah dibuat
    assert response.status_code in [200, 400]

    if response.status_code == 200:
        data = response.json()

        assert "message" in data
        assert data["message"] == "User created"


def test_login(client):
    response = client.post(
        "/auth/login",
        json={
            "email": "pytestuser@mail.com",
            "password": "123456"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert "token_type" in data
    assert data["token_type"] == "bearer"