import pytest
from dummy.models import DummyModel


@pytest.mark.django_db
def test_db_connection():
    DummyModel.objects.create(name="test")
    assert DummyModel.objects.count() == 1
