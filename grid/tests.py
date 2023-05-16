import pytest
from rest_framework.test import APIClient

from grid.models import Grid

# Create your tests here.

pytestmark = pytest.mark.django_db


def test_blank_input():
    client = APIClient()
    res = client.post("/api/v1/grid/", format="json")
    assert res.status_code == 400


def test_bad_input():
    client = APIClient()
    res = client.post("/api/v1/grid/", {"data": "abcd"}, format="json")
    assert res.status_code == 400
    res = client.post("/api/v1/grid/", {"data": "--12,4"}, format="json")
    assert res.status_code == 400


def test_successful():
    client = APIClient()
    res = client.post("/api/v1/grid/", {"data": "2,2;-1,30;20,11;4,5"}, format="json")
    assert res.status_code == 201
    grid = Grid.objects.get(data="2,2;-1,30;20,11;4,5")
    assert grid.closest == "2,2;4,5"
