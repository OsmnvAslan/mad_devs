from datetime import datetime

import pytest

from django.test.client import Client

from common.models import ExtendedUser, Diagnosis
from common.serializers.authorize_user import AuthorizeUser


@pytest.fixture
def user(db) -> ExtendedUser:
    return ExtendedUser.objects.create_user(
        username='user',
        password='pass',
        is_doctor=False,
        date_of_birth=datetime.now(),
    )


@pytest.fixture
def doctor(db) -> ExtendedUser:
    return ExtendedUser.objects.create_user(
        username='doctor',
        password='pass',
        is_doctor=True,
    )


@pytest.fixture
def doctor_client(db, doctor, client: Client) -> Client:
    token = AuthorizeUser.generate_token(user=doctor)
    client.defaults['HTTP_AUTHORIZATION'] = 'Bearer ' + token
    return client


@pytest.fixture
def diagnoses(db, user) -> None:
    Diagnosis.objects.create(user=user, name='ARVI')
    Diagnosis.objects.create(user=user, name='COVID')
    Diagnosis.objects.create(user=user, name='PTSD')
