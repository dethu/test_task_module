from helpers.simple_client import SimpleCalculateClient


# todo: Переименовать тесты, добавить проверку с jsonmap,

class TestCalculate(object):
    _client = SimpleCalculateClient("http://165.22.81.75:8090/test/calculate")

    def test_positive_200(self):
        """
        """
        response = self._client.calculate(2, 2, "*")
        assert (response.status_code == 200)

    def test_negative_400(self):
        """
        """
        response = self._client.calculate(2, 2, "%")
        assert (response.status_code == 200)
