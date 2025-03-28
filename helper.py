import random
import string
import allure
from faker import Faker

fake = Faker()

@allure.step("Генерируем логин из 12 символов")
def generate_login():
    return "".join(random.choice(string.ascii_lowercase) for _ in range(12)) #генерация логина, состоящего из рандомных букв

@allure.step("Генерируем пароль из 8 символов")
def generate_password():
    return fake.password(length=8, digits=True) #генерация пароля

@allure.step("Генерируем имя")
def generate_firstname():
    return fake.first_name() #генерация имени