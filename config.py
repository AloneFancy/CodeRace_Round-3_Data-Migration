import configparser
import re
def user_config():
    pass

def default_config():
    config = configparser.ConfigParser()
    config.read('a.conf')
    return config

default_config()