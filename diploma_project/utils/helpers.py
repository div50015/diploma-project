import logging
import json
import os
from diploma_project import utils
from pathlib import Path


SCHEMA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../json_schemas')


def load_schema(file_name):
    with open(os.path.join(SCHEMA_PATH, file_name)) as file:
        schema = json.load(file)
        return schema


def abs_path_from_project(relative_path: str):
        return (
        Path(utils.__file__).parent.parent.parent.joinpath(relative_path).absolute().__str__()
    )


def log_to_console(response):
    logging.info("Response text: %s", response.text)
    logging.info("Request URL: %s", response.request.url)
    logging.info("Response Code: %s", response.status_code)
