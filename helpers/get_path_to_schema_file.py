from os.path import dirname


def get_path_to_schema_file(tests_directory, schema_file_name, path_to_json_schemas='/schemas/'):
    return dirname(tests_directory) + path_to_json_schemas + schema_file_name
