import pytest

from class_yandex import YandexClass
from test_yandex import main

fixture_create = [
    ('test_1', 201),
    ('test_1', 409)
]
fixture_delete = [
    ('test_1', 204),
    ('test_1', 404)
]

# Для выполнения тестов необходимо поместить токен для Я.Диска в файл
# access_yandex.txt


class TestYandex:
    @pytest.mark.parametrize('folder_name, response_status_code',
                             fixture_create)
    def test_create_folder(self, folder_name, response_status_code):
        with open('..\\access_yandex.txt', 'r', encoding='utf-8') as file:
            token = file.read()
        test_1 = YandexClass(got_token=token)
        assert test_1.create_folder(folder_name) == response_status_code

    @pytest.mark.parametrize('folder_name, response_status_code',
                             fixture_delete)
    def test_delete_folder(self, folder_name, response_status_code):
        with open('..\\access_yandex.txt', 'r', encoding='utf-8') as file:
            token = file.read()
        test_1 = YandexClass(got_token=token)
        assert test_1.delete_folder(folder_name) == response_status_code

    @pytest.mark.xfail()
    def test_no_creation_without_authorization(self):
        test_no_auth = YandexClass(got_token=None)
        assert test_no_auth.create_folder('test_no_auth') == 401

    @pytest.mark.xfail()
    def test_no_creation_without_folder_name(self):
        with open('..\\access_yandex.txt', 'r', encoding='utf-8') as file:
            token = file.read()
        test_no_name = YandexClass(got_token=token)
        assert test_no_name.create_folder('') == 400


if __name__ == '__main__':
    main()
