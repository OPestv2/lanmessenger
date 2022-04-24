import json
import sys

"""
Globals parser uses config.json file to operate on specified values used in script processing
"""


class JSONParser:
    def __init__(self):
        self.config = self.__load_configuration()

    def backup_config(self):
        pass

    def restore_config(self):
        pass

    def load_config(self):
        pass

    def export_config(self):
        pass

    def put_json(self):
        pass

    def read_json(self, key_list):
        """
        Get value from config dictionary.

        :param key_list: List of keys that leads to value of key specified as the last one in list
        :type key_list: list
        :return: config value
        """

        # find (even deeply nested) value
        try:
            current_element = self.config
            for key in key_list:
                current_element = current_element[key]

            return current_element

        except KeyError:
            print("[!!!] Could not find key in configuration")
            sys.exit(0)
        except TypeError:
            print("[!!!] Encountered non dictionary element")
            sys.exit(0)

    def update_json(self):
        pass

    def delete_json(self):
        pass

    def __load_configuration(self):
        """
        Function loads content of config.json to object variable.

        :return: None
        """

        try:
            # load json file to variable
            with open("config.json", "r") as config_file:
                return json.load(config_file)
        except FileNotFoundError:
            print("[!!!] Config file unreachable.")
            sys.exit(0)
        except:
            print("[!!!] Unknown error encountered when parsing config.json file.")
            sys.exit(0)
