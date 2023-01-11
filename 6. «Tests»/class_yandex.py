import requests

# Для создания и удаления папок на сервере Я.Диска необходимо поместить
# авторизационный токен в файл access_yandex.txt


class YandexClass:
    link = 'https://cloud-api.yandex.net'

    def __init__(self, got_token):
        self.token = got_token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_folder(self, folder_name):
        url = '/v1/disk/resources'
        href = self.link + url
        params = {
            'path': folder_name,
            'overwrite': 'true'
        }
        res = requests.put(href, headers=self.headers, params=params)
        return res.status_code

    def delete_folder(self, folder_name):
        url = '/v1/disk/resources'
        href = self.link + url
        params = {'path': folder_name}
        res = requests.delete(href, headers=self.headers, params=params)
        return res.status_code


if __name__ == '__main__':
    with open('access_yandex.txt', 'r', encoding='utf-8') as file:
        token = file.read()

    new_folder = YandexClass(token)
    no_auth = YandexClass(got_token=None)
    # print(new_folder.create_folder('test_1'))
    # print(new_folder.create_folder('test_1'))
    # print(new_folder.delete_folder('test_1'))
    # print(new_folder.delete_folder('test_1'))
    # print(no_auth.create_folder('no_auth'))
    # print(new_folder.create_folder(''))
