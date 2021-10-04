import jwt
from django.urls import reverse
from django.test.client import Client
from django.conf import settings


def test_user_authorization(db, client: Client, user) -> None:
    path = reverse('login-list')
    payload = {
        'username': 'user',
        'password': 'pass',
    }
    response = client.post(
        path=path,
        data=payload,
        content_type='application/json',
    )
    assert response.status_code == 201
    json_response = response.json()
    jwt_token = json_response['access_token']
    decoded_token = jwt.decode(
        jwt=jwt_token, key=settings.SECRET_KEY, algorithms=[settings.ALGORITHM],
    )
    assert not decoded_token['is_doctor']


def test_user_authorization_doctor(db, client: Client, doctor) -> None:
    path = reverse('login-list')
    payload = {
        'username': 'user',
        'password': 'pass',
    }
    response = client.post(
        path=path,
        data=payload,
        content_type='application/json',
    )
    assert response.status_code == 201
    json_response = response.json()
    jwt_token = json_response['access_token']
    decoded_token = jwt.decode(
        jwt=jwt_token, key=settings.SECRET_KEY, algorithms=[settings.ALGORITHM],
    )
    assert decoded_token['is_doctor']
