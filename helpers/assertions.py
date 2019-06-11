import json
from os.path import join
from jsonschema import validate


def assert_valid_schema(data, schema_file):
    """
    Проверяем, что данные соответствуют jsonschem'е
    :param data: Данные для валидации, json
    :param schema_file: Схема валидации, json
    :return: результат валидации, логический
    """
    schema = _load_json_schema(schema_file)
    return validate(data, schema)


def _load_json_schema(filename):
    absolute_path = join(filename)
    with open(absolute_path) as schema_file:
        return json.loads(schema_file.read())