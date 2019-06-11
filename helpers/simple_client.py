import requests


# todo: Вынести генерацию данных в отдельную функцию

class SimpleCalculateClient(object):
    _base_url = ''
    _calculate_endpoint = ''

    def __init__(self, url):
        self._base_url = url

    def calculate(self, left_operand, right_operand, operation):
        data = {"left_operand": left_operand,
                "right_operand": right_operand,
                "operation": operation}
        return requests.post(self._base_url, json=data)