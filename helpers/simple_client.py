import requests


class SimpleCalculateClient(object):
    _url = ""
    _timeout = None

    def __init__(self, url, default_time_out=None):
        """
        :param url: URL метода, в который будет ходить клиент
        :param default_time_out: Таймаут по-умолчанию, который будет использовать клиент, можно не задавать,
               тогда таймаут будет бесконечным.
        """
        self._url = url
        self._timeout = default_time_out

    def calculate(self, expression, timeout=_timeout):
        try:
            response = requests.post(self._url, json=expression, timeout=timeout)
        except requests.ConnectionError as connection_error:
            print("Error Connecting:", connection_error)
        except requests.exceptions.Timeout as timeout:
            print("Timeout Error:", timeout)
        return response
