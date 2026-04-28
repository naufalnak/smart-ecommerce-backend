def test_create_category(client):
    response = client.post(
        "/categories/",
        json={
            "name": "Testing Category"
        }
    )

    assert response.status_code in [200, 400]


def test_create_product(client):
    response = client.post(
        "/products/",
        json={
            "name": "Gaming Mouse",
            "description": "Mouse for testing",
            "price": 100,
            "category_id": 1
        }
    )

    assert response.status_code in [200, 400]


def test_get_products(client):
    response = client.get("/products/")

    assert response.status_code == 200

    data = response.json()

    assert "data" in data