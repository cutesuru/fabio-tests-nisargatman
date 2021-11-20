import pytest
from wikiapp.models import Continent,Country,City
pytestmark = pytest.mark.django_db

def test_get_absolute_url(user: User):
    assert Country.get_absolute_url() == f"/country/{Country.uuid}/"
    assert Continent.get_absolute_url() == f"/continent/{Continent.uuid}/"
    assert City.get_absolute_url() == f"/city/{City.uuid}/"