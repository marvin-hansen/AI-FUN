import os
import configparser
from enum import Enum, unique, auto
from pathlib import Path


@unique
class KEYS(Enum):
    """ ENUM to encode valid keys """
    TWITTER = auto()



DBG = True
twt_key_file = "twitter.key"


def set_key(key: KEYS, key_folder: str = "keys"):
    """
    :param key:
    :param key_folder:
    :return:
    """
    if key is KEYS.TWITTER:
        return load_key(k_file=twt_key_file, k_folder=key_folder)


def load_key(k_file: str = None, k_folder: str = "keys"):
    """
    Set access key to either the provided string or loads from a local file containing the string.
    Note, the file must be created with "store_key" to ensure proper reading.

    :param k_folder: key folder
    :param k_file: key_file containing the key
    :return: str key loaded from file
    """
    if k_file is None:
        print("Please pass a path to a key file to load a key")

    if k_folder is None:
        print("Please pass a folder to a key file to load a key")

    else:
        if not os.path.exists(k_folder):
            print("Key folder does not exists")

        path = Path(k_folder + "/" + k_file)
        exists: bool = os.path.isfile(path)

        if not exists:
            print("Key file does not exists: " + k_file)

        else:
            if DBG:
                print("Loading key from from file: " + str(path))
                config = configparser.ConfigParser()
                config.read(path)
                api_key = config['TWITTER']['API_KEY']
                api_secret_key = config['TWITTER']['API_SECRET_KEY']
                access_token_key = config['TWITTER']['ACCESS_TOKEN']
                access_token_secret = config['TWITTER']['ACCESS_TOKEN_SECRET']

            return api_key, api_secret_key, access_token_key, access_token_secret
