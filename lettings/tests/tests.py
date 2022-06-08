import pytest

from django.urls import reverse
from django.test import Client

from lettings.models import Letting, Address


@pytest.fixture
def address(db) -> Address:
    return Address.objects.create(
        number=12529,
        street="State Road 535",
        city="Orlando",
        state="FL",
        zip_code=32836,
        country_iso_code="USA",

    )


@pytest.fixture
def letting(db, address) -> Letting:
    return Letting.objects.create(title="Lake Buena Vista", address=address)


def test_letting_list_view(letting):
    client = Client()

    path = reverse('lettings_index')
    response = client.get(path)
    content = response.content.decode()

    assert response.status_code == 200
    assert "<title>Lettings</title>" in content
    assert letting.title in content


def test_letting_detail_view(letting):
    client = Client()

    path = reverse('letting', kwargs={'letting_id': letting.id})
    response = client.get(path)
    content = response.content.decode()

    assert response.status_code == 200
    assert f'<title>{letting.title}</title>' in content
