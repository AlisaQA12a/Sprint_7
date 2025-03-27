import allure
import pytest
import requests

from data import DataMessage
from helper import generate_login, generate_password
from urls import Urls


class TestCourierLogin:

    @allure.title("Успешная авторизация курьера, если все обязательные поля заполнены")
    def test_login_courier(self, auth_data):
        response = requests.post(f"{Urls.BASE}{Urls.COURIER_LOGIN}", data=auth_data)
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
        response = requests.post(f"{Urls.BASE}{Urls.COURIER_LOGIN}", data=data)
        assert response.status_code == 404 and DataMessage.MESSAGE_ACCOUNT_NOT_FOUND in response.json().get("message")

    @allure.title("Получение ошибки  с пустыми полями логина или пароля при авторизации")
    @pytest.mark.parametrize(
        "login_data",
        [
            {"login": ""},
            {"password": ""},
        ],
    )
    def test_login_courier_empty_params(self, login_data, auth_data):
        data = auth_data.copy()
        data.update(login_data)
        response = requests.post(f"{Urls.BASE}{Urls.COURIER_LOGIN}", data=data)
        assert response.status_code == 400 and DataMessage.MESSAGE_NOT_ENOUGH_LOGIN_DATA in response.json().get("message")

    @allure.title("Получение ошибки авторизации, если данные о логине и пароле отсутствуют")
    @pytest.mark.parametrize(
        "login_fields",
        [
            "login",  # удаляем логин из данных
            "password",  # удаляем пароль из данных
        ],
    )
    def test_login_courier_empty_params(self, login_fields, auth_data):
        data = auth_data.copy()
        data.pop(login_fields)
        response = requests.post(f"{Urls.BASE}{Urls.COURIER_LOGIN}", data=data)
        #на момент запуска тест падал, возвращая код ошибки 504 (gateway time out) вместо ожидаемого 400
        assert response.status_code == 400 and DataMessage.MESSAGE_NOT_ENOUGH_LOGIN_DATA in response.json().get("message")