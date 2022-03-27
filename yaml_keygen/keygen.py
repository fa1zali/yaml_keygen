# Author: Faisal Ali
# Creation Date: Mar, 26 2022
# Version: 0.1.6
# Revision Date: Mar, 27 2022

# Import libraries
import ruamel.yaml


class YAML:

    # Creating an empty list for storing keys extracted from YAML
    keys = list()

    def read(self, filename: str) -> dict:
        """
        Takes the path and filename for the YAML, reads it and returns a python dictionary.

        ### Parameters
        - filename : str
            - Path and filename for YAML.

        ### Returns
        - dict
            - A dictionary object for the YAML.
        """
        try:
            YAML.keys.clear()
            with open(filename) as file:
                object = ruamel.yaml.load(
                    file, Loader=ruamel.yaml.RoundTripLoader, preserve_quotes=True)
                return object

        except Exception as error:
            print(f"Unable to read the file: {error}")
            quit()

    def get_keys(self, data: dict, sep=">", _prefix="") -> list:
        """
        Iterate over all the key value pairs in a YAML dictionary and returns the keys.

        ### Parameters
        - data : dict
            - YAML in dictionary format.
        - sep : str, (default ">")
            - Used for separating the nested keys.
        - _prefix : str
            - Not to be modified by user. For internal use

        ### Returns
        - List
            - List of keys from the YAML.
        """
        try:
            if isinstance(data, dict):
                for k, v2 in data.items():
                    res = not bool(v2)
                    p2 = f"{_prefix} {k}"
                    if res == True:
                        tmp1 = p2.strip()
                        tmp2 = tmp1.split(" ")
                        YAML.keys.append(sep.join(tmp2))
                    else:
                        self.get_keys(v2, sep, p2)

            elif isinstance(data, list):
                for i, v2 in enumerate(data):
                    p2 = f"{_prefix} {i}"
                    self.get_keys(v2, sep, p2)

            else:
                tmp1 = _prefix.strip()
                tmp2 = tmp1.split(" ")
                YAML.keys.append(sep.join(tmp2))

            return YAML.keys

        except Exception as error:
            print(f"Unable to traverse the nested dictionary: {error}")
            quit()

    def to_text(self, data: list, filename: str) -> object:
        """
        Saves the data to a text file.

        ### Parameters
        - data : list
            - Data in the form of list (YAML Keys).
        - filename : str
            - Path and filename of the TXT file

        ### Returns
        - TXT File
            - A TXT file is returned with the keys.
        """
        with open(filename, mode="w+") as txt_file:
            for elm in data:
                txt_file.write(f"{elm}\n")
