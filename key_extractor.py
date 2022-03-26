# Author: Faisal Ali
# Creation Date: Mar, 26 2022
# Version: 0.1.2
# Revision Date: NA

# Import libraries
from tkinter.tix import TEXT
import ruamel.yaml

# Creating an empty list for storing keys
yaml_keys = list()


def reader(filename: str) -> dict:
    """
    Takes the path and filename for the YAML, reads the same and returns a python dictionary.

    filename: path and filename for YAML.

    return: dict of the YAML.
    """

    try:
        yaml_keys.clear()
        with open(filename) as file:
            yaml_object = ruamel.yaml.load(
                file, Loader=ruamel.yaml.RoundTripLoader, preserve_quotes=True)
            return yaml_object

    except Exception as error:
        print(f"Unable to read the file: {error}")
        quit()


def key_extraction_yaml_obj(yaml_dict: dict, prefix="") -> list:
    """
    Iterate over all the key value pairs in a YAML dictionary and returns the keys.

    yaml_dict: YAML in dict() format.

    return: list of keys from the YAML.
    """
    try:
        if isinstance(yaml_dict, dict):
            for k, v2 in yaml_dict.items():
                res = not bool(v2)
                p2 = f"{prefix} {k}"
                if res == True:
                    tmp1 = p2.strip()
                    tmp2 = tmp1.split(" ")
                    yaml_keys.append(">".join(tmp2))
                else:
                    key_extraction_yaml_obj(v2, p2)

        elif isinstance(yaml_dict, list):
            for i, v2 in enumerate(yaml_dict):
                p2 = f"{prefix} {i}"
                key_extraction_yaml_obj(v2, p2)

        else:
            tmp1 = prefix.strip()
            tmp2 = tmp1.split(" ")
            yaml_keys.append(">".join(tmp2))

        return yaml_keys

    except Exception as error:
        print(f"Unable to traverse the nested dictionary: {error}")
        quit()


def key_extraction_yaml_file(filename: str) -> list:
    """
    Iterate over all the key value pairs in a YAML file and returns the keys.

    filename: path and filename for YAML.

    return: list of keys from the YAML.
    """

    yaml_object = reader(filename)
    keys = key_extraction_yaml_obj(yaml_dict=yaml_object)
    return keys
