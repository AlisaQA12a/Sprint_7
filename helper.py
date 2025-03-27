import random
import string
from faker import Faker

fake = Faker()


def generate_login():
    return "".join(random.choice(string.ascii_lowercase) for _ in range(12)) #генерация логина, состоящего из рандомных букв


def generate_password():
    return fake.password(length=8, digits=True) #генерация пароля


def generate_firstname():
    return fake.first_name() #генерация имени