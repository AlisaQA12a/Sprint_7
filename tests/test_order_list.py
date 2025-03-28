import allure
import requests

from urls import Urls


class TestOrderList:

    @allure.title("Получаем список заказов")
    def test_get_order_list(self):
        response = requests.get(Urls.GET_ORDERS_LIST)
        assert response.status_code == 200 and isinstance(response.json()["orders"], list)