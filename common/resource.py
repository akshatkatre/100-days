import json
import os

PATH = '/Users/akshat/PycharmProjects/my_resources.json'


def get_resource_key(resource: str) -> str:
    with open(PATH) as file_handle:
        data = json.load(file_handle)
    return data[resource]