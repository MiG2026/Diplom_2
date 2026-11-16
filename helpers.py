import time
import random
from faker import Faker

fake = Faker()
fakeRU = Faker(locale='ru_RU')


def create_random_email():
    name = fake.user_name()
    return f'{name}_{int(time.time())}_{random.randint(100, 999)}@yandex.ru'


def create_random_password():
    password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return password


def create_random_username():
    username = fakeRU.first_name()
    return username
