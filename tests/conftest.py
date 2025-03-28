import pytest
import requests

from helper import generate_login, generate_password, generate_firstname
from urls import Urls


@pytest.fixture(scope="session")
def auth_data():
    # генерация курьера с валидными данными
    courier_data = {
        "login": generate_login(),
        "password": generate_password(),
        "firstName": generate_firstname(),
    }
    auth_data = {key: value for key, value in courier_data.items() if key in ("login", "password")}

    # создание тестового курьера
    response = requests.post(Urls.COURIER_CREATE, data=courier_data)
    if response.status_code != 201:
        raise RuntimeError(
            f"Упс, не удалось создать тестового курьера! {response.status_code}: {response.text}"
        )

    # получение айди курьера, для этого надо залогиниться
    response = requests.post(Urls.COURIER_LOGIN, data=auth_data)
    courier_id = response.json().get("id")

    # выполнение теста
    yield auth_data

    # удаление  тестового курьера
    requests.delete(f"{Urls.COURIER_DELETE}/{courier_id}")