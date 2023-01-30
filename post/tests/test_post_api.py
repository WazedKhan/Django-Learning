import pytest

from django.urls import reverse

from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_create_new_post():
    payload = {"title": "New Post", "content": "Some Content"}
    response = client.post("", payload)
    data = response.data  # type: ignore
    assert data["title"] == payload["title"]


@pytest.mark.django_db
def test_get_posts(post):
    response = client.get("")
    assert response.status_code == 200  # type: ignore
    assert response.data[0]["title"] == post.title  # type: ignore
