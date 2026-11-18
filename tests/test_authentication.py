from conftest import *


class TestAuthentication:
    @allure.title('Проверка успешной аутентификации пользователя при передаче валидных данных созданного аккаунта')
    @allure.description('Аккаунт для проверки создается фикстурой перед тестом и удаляется после. '
                        'В ответе проверяются код и тело, в том числе получение accessToken и refreshToken')
    def test_auth_existing_account_success(self, create_new_user_and_delete):
        payload = create_new_user_and_delete[0]

        @allure.step('Аутентификация пользователя по email и паролю')
        def send_post_user_auth():
            return requests.post(Urls.user_auth, data=payload)

        response = send_post_user_auth()
        deserials = response.json()
        assert response.status_code == 200
        assert deserials['success'] is True
        assert 'accessToken' in deserials.keys()
        assert 'refreshToken' in deserials.keys()
        assert deserials['user']['email'] == payload['email']
        assert deserials['user']['name'] == payload['name']

    @allure.title('Проверка ответа на запрос аутентификации с незарегистрированным email')
    def test_auth_with_wrong_login_expected_error(self):
        payload = {
            'email': create_random_email(),
            'password': UsersData.password,}

        @allure.step('Аутентификация пользователя с незарегистрированным email')
        def send_post_user_auth():
            return requests.post(Urls.user_auth, data=payload)

        response = send_post_user_auth()
        assert response.status_code == 401 and response.json() == {"success": False, "message": "email or password are incorrect"}

    @allure.title('Проверка ответа на запрос аутентификации с неверным паролем')
    def test_auth_with_wrong_passwd_expected_error(self):
        payload = {
            'email': UsersData.email,
            'password': create_random_password(),}

        @allure.step('Аутентификация пользователя с неверным паролем')
        def send_post_user_auth():
            return requests.post(Urls.user_auth, data=payload)

        response = send_post_user_auth()
        assert response.status_code == 401 and response.json() == {"success": False, "message": "email or password are incorrect"}