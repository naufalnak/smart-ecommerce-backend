def get_auth_token(client):
    login_response = client.post(
        "/auth/login",
        json={
            "email": "pytestuser@mail.com",
            "password": "123456"
        }
    )

    token = login_response.json()["access_token"]

    return token

def test_add_to_cart(client):
    token = get_auth_token(client)

    response = client.post(
        "/cart/",
        json={
            "product_id": 1,
            "quantity": 2
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code in [200, 400]
    
def test_get_cart(client):
    token = get_auth_token(client)

    response = client.get(
        "/cart/",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200
    
def test_checkout(client):
    token = get_auth_token(client)

    response = client.post(
        "/orders/checkout",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code in [200, 400]

    if response.status_code == 200:
        data = response.json()

        assert "message" in data