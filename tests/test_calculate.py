import pytest
from helpers.simple_client import SimpleCalculateClient
from helpers.expression_generator import generate_expression
from helpers.assertions import assert_valid_schema
from helpers.get_path_to_schema_file import get_path_to_schema_file


# todo: Переименовать тесты, добавить проверку с jsonmap,

class TestCalculate(object):
    _client = SimpleCalculateClient("http://165.22.81.75:8090/test/calculate")

    @pytest.mark.parametrize(
        'left_operand, right_operand, operation, result', [
            (2, 2, "*", 4),
            (4, 2, "/", 2),
            (2, 5, "+", 7),
            (2, 2, "-", 0),
        ]
    )
    def test_should_calculate_correctly_and_return_200_while_expression_is_valid(self, left_operand, right_operand, operation, result):
        response = self._client.calculate(generate_expression(left_operand, right_operand, operation))
        assert (response.status_code == 200)
        assert_valid_schema(response.json(), get_path_to_schema_file(__file__, 'calculate_correct_200_response'))
        assert (response.json()["result"] == result)

    def test_should_return_400_for_expression_with_unsupported_operation(self):
        response = self._client.calculate(generate_expression(2, 2, "%"))
        assert (response.status_code == 400)
        assert_valid_schema(response.json(), get_path_to_schema_file(__file__, 'calculate_error_400_response'))
        # Я не уверен, что человеко-читаемые ошибки - это часть контракта.
        assert (response.json()["error"] == "\"operation\" value must be one of \"['-', '+', '/', '*']\"")

    def test_should_return_400_for_invalid_expression(self):
        incorrect_expression = {"left_operand": 1, "right_operand": 2}
        response = self._client.calculate(incorrect_expression)
        assert (response.status_code == 400)
        assert_valid_schema(response.json(), get_path_to_schema_file(__file__, 'calculate_error_400_response'))
        # Я не уверен, что человеко-читаемые ошибки - это часть контракта.
        assert (response.json()["error"] == "\"operation\" is not specified in request body")

