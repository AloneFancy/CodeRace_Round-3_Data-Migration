import configparser

def load_config(profile='DEFAULT'):
    """
    Loading the configuration file
    """
    
    config = configparser.ConfigParser()
    config.read('keys.conf')    
    if not config.has_section(profile) and profile!='DEFAULT':    
        raise Exception("Profile \'"+ profile +"\' does not exists")
    
    return config[profile]

def load_config_value():
    """
    Config Values for RST file    
    """
    config = configparser.ConfigParser()
    config.read('values.conf')  
    return config['RST']  

