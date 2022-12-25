import unittest
import requests
from unittest.case import TestCase

from main import filtering_by_geo, searching_uniq, main_channel, create_folder

class TestMain(TestCase):
    def test_filtering_by_geo(self):
        res = filtering_by_geo()
        for item in res:
            self.assertIsInstance(list(item.values())[0][1], str, "Россия")

    def test_searching_uniq(self):
        res = searching_uniq()
        for item in res:
            self.assertEqual(res.count(item), 1)

    def test_main_channel(self):
        stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
        res = main_channel()
        biggest_traffic = stats.get(res)
        for key, value in stats.items():
            self.assertGreaterEqual(biggest_traffic, value)

    def test_create_folder(self):
        # Проверяем код ответа на запрос о создании папки
        res = create_folder()
        self.assertMultiLineEqual(str(res), '<Response [201]>')

        # Проверяем, что папка появилась на Диске. Для этого запрашиваем сведения о папке, если проходят, значит, папка существует.
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        token = token =           #!!!!!!!!!!!!!!!!!!  Введите токен с Яндекса !!!!!!!!!!!!!!!!
        folder_name = 'my_folder'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {token}'
        }
        result = requests.get(f'{url}?path={folder_name}', headers=headers)
        self.assertMultiLineEqual(str(result), '<Response [200]>')








