import pytest
import allure
import requests

from data import DataOrders
from urls import Urls


class TestCreateOrder:

    @allure.title("Cозданиe заказа с разными цветами самоката")
    @pytest.mark.parametrize(
        "order_data",
        [
            DataOrders.CREATE_ORDER_NO_COLORS,
            DataOrders.CREATE_ORDER_BLACK_COLOR,
            DataOrders.CREATE_ORDER_GREY_COLOR,
            DataOrders.CREATE_ORDER_TWO_COLORS,
        ],
    )
    def test_create_order(self, order_data):
        headers = {"Content-Type": "application/json"}
        response = requests.post(Urls.GET_ORDERS_LIST, json=order_data, headers=headers)
        assert response.status_code == 201
        r = response.json()
        assert "track" in r and isinstance(r["track"], int)