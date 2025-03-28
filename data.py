class DataMessage:
    MESSAGE_ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
    MESSAGE_NOT_ENOUGH_LOGIN_DATA = "Недостаточно данных для входа"
    MESSAGE_LOGIN_IS_USED = "Этот логин уже используется"
    MESSAGE_CREATE_COURIER_MISSED_DATA = "Недостаточно данных для создания учетной записи"


class DataOrders:
    #заказ без указания цвета
    CREATE_ORDER_NO_COLORS = {
        "firstName": "Гарри",
        "lastName": "Шпротер",
        "address": "улица Веселая, 35",
        "metroStation": 2,
        "phone": "+7 903 223 57 57",
        "rentTime": 3,
        "deliveryDate": "2025-07-22",
        "comment": "Хочу на море",
        "color": [],
    }

    #заказ  самоката цвета "серая безысходность"
    CREATE_ORDER_GREY_COLOR = {
        "firstName": "Яша",
        "lastName": "Рыжий",
        "address": "проспект Корма , 29",
        "metroStation": 5,
        "phone": "+7 906 555 55 55",
        "rentTime": 2,
        "deliveryDate": "2025-05-27",
        "comment": "Помогите",
        "color": ["GREY"],
    }

    #заказ самоката цвета "черный жемчуг"
    CREATE_ORDER_BLACK_COLOR = {
        "firstName": "Лето",
        "lastName": "Хочу",
        "address": "улица Морская, 69",
        "metroStation": 4,
        "phone": "+7 902 123 12 34",
        "rentTime": 1,
        "deliveryDate": "2025-09-18",
        "comment": "Ничего не успеваю",
        "color": ["BLACK"],
    }
    #выбор обоих цветов при заказе самоката
    CREATE_ORDER_TWO_COLORS = {
        "firstName": "Спам",
        "lastName": "Спамович",
        "address": "проспект Сна, 8",
        "metroStation": 1,
        "phone": "+7 999 654 32 11",
        "rentTime": 4,
        "deliveryDate": "2025-10-11",
        "comment": "Боже, дай мне сил",
        "color": ["BLACK", "GREY"],
    }