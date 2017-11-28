import pytest


def pytest_collection_modifyitems(items):
    for item in items:
        item.keywords['django_db'] = pytest.mark.django_db
