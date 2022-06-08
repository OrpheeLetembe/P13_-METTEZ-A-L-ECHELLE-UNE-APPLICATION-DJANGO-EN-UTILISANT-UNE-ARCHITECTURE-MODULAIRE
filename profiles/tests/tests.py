import pytest

from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User

from profiles.models import Profile


@pytest.fixture
def user(db) -> User:
    return User.objects.create_user(username='stan',
                                    password='stan123654',
                                    email='stan@gmailcom',
                                    last_name='Smith',
                                    first_name='stan'
                                    )


@pytest.fixture
def profile(db, user) -> Profile:
    return Profile.objects.create(user=user, favorite_city='London')


def test_profile_list_view(profile):
    client = Client()

    path = reverse('profiles_index')
    response = client.get(path)
    content = response.content.decode()

    assert response.status_code == 200
    assert "<title>Profiles</title>" in content
    assert profile.user.username in content


def test_profile_detail_view(profile):
    client = Client()

    path = reverse('profile', kwargs={'username': profile.user.username})
    response = client.get(path)
    content = response.content.decode()

    assert response.status_code == 200
    assert f'<title>{profile.user.username}</title>' in content
