import allure
import pytest
import requests

from data import DataMessage
from helper import generate_login, generate_password
from urls import Urls


class TestCourierLogin:

    @allure.title("Успешная авторизация курьера, если все обязательные поля заполнены")
    def test_login_courier(self, auth_data):
        response = requests.post(Urls.COURIER_LOGIN, data=auth_data)
        assert response.status_code == 200 and "id" in response.json()

    @allure.title("Получение ошибки при неправильных данных в полях логин или пароль")
    @pytest.mark.parametrize(
        "login_data",
        [
            {"login": generate_login()},
            {"password": generate_password()},
        ],
    )
    def test_login_courier_with_wrong_params(self, login_data, auth_data):
        data = auth_data.copy()
        data.update(login_data)
        response = requests.post(Urls.COURIER_LOGIN, data=data)
        assert response.status_code == 404 and DataMessage.MESSAGE_ACCOUNT_NOT_FOUND in response.json().get("message")

    @allure.title("Получение ошибки  с пустыми полями логина или пароля при авторизации")
    @pytest.mark.parametrize(
        "login_data",
        [
            {"login": ""},
            {"password": ""},
            "login",  # удаляем логин из данных
            "password",  # удаляем пароль из данных
        ],
    )
    def test_login_courier_empty_params(self, login_data, auth_data):
        data = auth_data.copy()

        if isinstance(login_data, str):
            del data[login_data]
        else:
            data.update(login_data)

        response = requests.post(Urls.COURIER_LOGIN, data=data)
        assert response.status_code == 400 and DataMessage.MESSAGE_NOT_ENOUGH_LOGIN_DATA in response.json().get("message")
