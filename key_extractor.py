# Author: Faisal Ali
# Creation Date: Mar, 26 2022
# Version: 0.1.1
# Revision Date: NA

# Import libraries
import ruamel.yaml


class YAMLOperations:
    """
    Used for performing YAML operations.
    """

    def reader(filename: str) -> dict:
        """
        Takes the path and filename for the YAML,
        reads the same and returns a python dictionary.
        :param filename: path and filename for YAML
        :return: dict of the YAML
        """

        try:
            with open(filename) as file:
                yaml_object = ruamel.yaml.load(
                    file, Loader=ruamel.yaml.RoundTripLoader, preserve_quotes=True)
                return yaml_object

        except Exception as error:
            print(f"Unable to read the file: {error}")
            quit()
