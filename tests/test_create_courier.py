import allure
import pytest
import requests

from data import DataMessage
from urls import Urls

from helper import generate_login, generate_password, generate_firstname


class TestCreateCourier:

    @allure.title("Успешно созданем курьера")
    @allure.description("Передаем все обязательные поля")
    def test_create_courier(self):
        payload = {
            "login": generate_login(),
            "password": generate_password(),
            "firstName": generate_firstname(),
        }
        response = requests.post(Urls.COURIER_CREATE, data=payload)
        assert response.status_code == 201 and response.json().get("ok") is True

    @allure.title("Нельзя создать двух одинаковых курьеров")
    @allure.description("Возвращается ошибка при создании курьера с уже существующим логином")
    def test_impossible_to_create_same_couriers(self, auth_data):
        payload = {
            "login": auth_data["login"],
            "password": generate_password(),
            "firstName": generate_firstname(),
        }
        response = requests.post(Urls.COURIER_CREATE, data=payload)
        assert response.status_code == 409 and DataMessage.MESSAGE_LOGIN_IS_USED in response.json().get("message")

    @allure.title("Получение ошибки,если  при создании пользователя не указывать одно из обязательных полей")
    @pytest.mark.parametrize(
        "signup_data",
        [
            {  # пустой логин
                "login": "",
                "password": generate_password(),
                "firstName": generate_firstname(),
            },
            {  # пустой пароль
                "login": generate_login(),
                "password": "",
                "firstName": generate_firstname(),
            },
            {  # не передаем логин
                "password": generate_password(),
                "firstName": generate_firstname(),
            },
            {  # не передаем пароль
                "login": generate_login(),
                "firstName": generate_firstname(),
            },
        ],
    )
    def test_can_not_create_courier_with_empty_input(self, signup_data):
        response = requests.post(Urls.COURIER_CREATE, data=signup_data)
        assert (
                response.status_code == 400
                and DataMessage.MESSAGE_CREATE_COURIER_MISSED_DATA in response.json().get("message")
        )  # fmt: skip
