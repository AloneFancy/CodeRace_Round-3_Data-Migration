import configparser
import globals

def load_config(profile='DEFAULT'):
    """
    Loading the configuration file
    """
    
    config = configparser.ConfigParser()
    config.read('a.conf')    
    if not config.has_section(profile) and profile!='DEFAULT':    
        raise Exception("Profile's name does not exists")
    return config


