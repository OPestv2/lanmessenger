import json
import os
import sys

from Static import ABS_PATH

"""
Globals parser uses config.json file to operate on specified values used in script processing
"""


class JSONParser:
    def __init__(self):
        self.config_path = ABS_PATH + "config.json"
        self.config = self.__load_configuration()

    def restore_config(self):
        pass

    def load_config(self):
        pass

    def export_config(self):
        pass

    # def put_json(self, key_list, value):
    #     """
    #     Insert value to specified key. Last key in key_list should be a new key and value be it's value
    #
    #     :param key_list: List of keys that leads to
    #     :param value:
    #     :return:
    #     """

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

    def update_json(self, key_list, value):
        """
        Update value in config. Last key in key_list should point to node whose value will be replaced

        :param key_list: List of keys that leads to value of key specified as the last one in list which will be replaced
        :type key_list: list
        :param value: New value
        :type value: object
        :return: None
        """

        # find nested value
        try:
            current_element = self.config
            for key in key_list[:-1]:
                current_element = current_element[key]

            # one before last key is reference
            current_element[key_list[-1]] = value
            self.__save()

        except KeyError:
            print("[!!!] Could not find key in configuration")
            sys.exit(0)
        except TypeError:
            print("[!!!] Encountered non dictionary element")
            sys.exit(0)

    def delete_json(self):
        pass

    def __load_configuration(self):
        """
        Function loads content of config.json to object variable.

        :return: None
        """

        try:
            # load json file to variable
            with open(self.config_path, "r") as config_file:
                return json.load(config_file)
        except FileNotFoundError:
            print("[!] Config file not found.")
            self.__create_new_config()
        except:
            print("[!!!] Unknown error encountered when parsing config.json file.")
            sys.exit(0)

    def __create_new_config(self):
        """
        If config file does not exist create new one

        :return: None
        """
        # save new config
        self.config = {'user': None}
        self.__save()

        # restart
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

    def __save(self):
        """
        Save changed config to config.json file.

        :return: None
        """
        try:
            # config dict to string
            config_str = json.dumps(self.config)

            # overwrite config
            with open(self.config_path, "w") as config_file:
                config_file.write(config_str)
        except:
            print("[!!!] Unknown error encountered when parsing config.json file.")
            sys.exit(0)