import pytest
from helpers.simple_client import SimpleCalculateClient
from helpers.expression_generator import generate_expression
from helpers.assertions import assert_valid_schema
from helpers.get_path_to_schema_file import get_path_to_schema_file


class TestCalculate(object):
    _client = SimpleCalculateClient("http://165.22.81.75:8090/test/calculate", 30)

    # я бы вынес эти тест-кейсы в юнит тесты. Тут оставил только 1.
    # Это скорее, как пример генерации тестов через параметры
    @pytest.mark.parametrize(
        'left_operand, right_operand, operation, result', [
            (2, 2, "*", 4),
            (4, 2, "/", 2),
            (2, 5, "+", 7),
            (2, 2, "-", 0),
        ]
    )
    def test_should_calculate_correctly_and_return_200_while_expression_is_valid(self, left_operand, right_operand,
                                                                                 operation, result):
        """
        Должны возвращать корректный результат и Ok(200),
        когда получили валидное выражение с поддерживаемыми операторами
        """
        response = self._client.calculate(generate_expression(left_operand, right_operand, operation), 0.00001)
        assert (response.status_code == 200)
        assert_valid_schema(response.json(), get_path_to_schema_file(__file__, 'calculate_correct_200_response'))
        assert (response.json()["result"] == result)

    def test_should_return_400_for_expression_with_unsupported_operation(self):
        """
        Должны возвращать Bad Request(400), когда получили выражение с неподдерживаемой операцией
        """
        response = self._client.calculate(generate_expression(2, 2, "%"))
        assert (response.status_code == 400)
        assert_valid_schema(response.json(), get_path_to_schema_file(__file__, 'calculate_error_400_response'))
        # Я не уверен, что человеко-читаемые ошибки - это часть контракта.
        # Поэтому не уверен, что нужно проверять текст ошибки на полное совпадение
        assert (response.json()["error"] == "\"operation\" value must be one of \"['-', '+', '/', '*']\"")

    def test_should_return_400_for_invalid_expression(self):
        """
        Должны возвращать Bad Request(400), когда получили невалидное выражение
        """
        response = self._client.calculate({"left_operand": 1, "right_operand": 2})
        assert (response.status_code == 400)
        assert_valid_schema(response.json(), get_path_to_schema_file(__file__, 'calculate_error_400_response'))
        # Я не уверен, что человеко-читаемые ошибки - это часть контракта.
        # Поэтому не уверен, что нужно проверять текст ошибки на полное совпадение
        assert (response.json()["error"] == "\"operation\" is not specified in request body")
