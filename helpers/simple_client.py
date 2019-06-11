import requests


class SimpleCalculateClient(object):
    _url = ""

    def __init__(self, url):
        self._url = url

    def calculate(self, expression, timeout=None):
        try:
            response = requests.post(self._url, json=expression, timeout=timeout)
        except requests.ConnectionError as connection_error:
            print("Error Connecting:", connection_error)
        except requests.exceptions.Timeout as timeout:
            print("Timeout Error:", timeout)
        return response
