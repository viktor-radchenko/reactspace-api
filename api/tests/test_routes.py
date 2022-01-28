import pytest

from django.urls import reverse


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


def test_product_routes(db, api_client):
    url = reverse('get_all_products')
    response = api_client.get(url)
    assert response.status_code == 200

    url = reverse('get_product', args=('1',))
    response = api_client.get(url)
    assert response.status_code == 200
    # this route will return error details since no products are created yet
    detail = response.data.get("detail")
    assert detail

    assert b'detail' in response.content
