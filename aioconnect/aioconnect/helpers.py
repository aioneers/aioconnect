"""Extract nested values from a JSON tree."""
import requests
import json


def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values


def get_values(json_data: list, key: str = "_id") -> list:
    """get_value [summary]

    Parameters
    ----------
    json_data : list
        [description]
    key : str, optional
        [description], by default "_id"

    Returns
    -------
    list
        [description]
    """

    if key == "":
        raise ValueError

    ret_list = []
    count = len(json_data)
    for i in range(0, count):
        x = json_data[i][key]
        ret_list.append(x)
    return ret_list
