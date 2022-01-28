import uuid

import pytest

from django.urls import reverse
from django.contrib.auth import get_user_model


@pytest.fixture
def test_password():
    return 'test-strong-password'


@pytest.fixture
def create_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        kwargs['password'] = test_password
        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())
        if 'email' not in kwargs:
            kwargs['email'] = 'test@test.com'
        if 'first_name' not in kwargs:
            kwargs['first_name'] = "Sam"
        if 'is_active' not in kwargs:
            kwargs['is_active'] = True
        return django_user_model.objects.create_user(**kwargs)
    return make_user


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.mark.django_db
def test_create_user():
    User = get_user_model()
    user = User.objects.create_user(
        email="test@test.com",
        username="test_user",
        first_name="First",
        password="foobar",
    )
    assert user.email == "test@test.com"
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser


@pytest.mark.django_db
def test_create_super_user():
    User = get_user_model()
    admin_user = User.objects.create_superuser(
        email="super@user.com",
        username="test_admin",
        first_name="Admin",
        password="foo",
    )
    assert admin_user.email == "super@user.com"
    assert admin_user.is_active
    assert admin_user.is_staff
    assert admin_user.is_superuser
