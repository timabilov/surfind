from django.test import TestCase

# Create your tests here.
from app.views import ContentViewSet


def test_content(rf):
    request = rf.get('/content/')
    response = ContentViewSet.as_view({"get": "list"})(request)
    assert response.status_code == 200


def test_dummy():

    assert 2 == 2

def test_dummy2():

    assert 2 == 2