from helpers import *


class UsersData:
    email = 'pud-8888@yandex.ru.ru'
    password = 'qwerty'
    username = 'psish'

    credentials_with_empty_field = [
        {'email': '',
         'password': create_random_password(),
         'name': create_random_username()
         },
        {'email': create_random_email(),
         'password': '',
         'name': create_random_username()
         },
        {'email': create_random_email(),
         'password': create_random_password(),
         'name': ''
         }
    ]


class IngredientData:
    burger_1 = ['6ae327a87e8698001b542b38', '6ae327a87e8698001b542b3d',
                '6ae327a87e8698001b542b3f', '6ae327a87e8698001b542b45']

    burger_2 = ['6ae327a87e8698001b542b39', '6ae327a87e8698001b542b3b',
                '6ae327a87e8698001b542b3e', '6ae327a87e8698001b542b43']

    invalid_hash_ingredient = '61c0c5a71d1f088005553535'
