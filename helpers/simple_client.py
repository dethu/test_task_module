import requests


# todo: Вынести генерацию данных в отдельную функцию

class SimpleCalculateClient(object):
    _url = ""

    def __init__(self, url):
        self._url = url

    def calculate(self, expression):
        return requests.post(self._url, json=expression)
