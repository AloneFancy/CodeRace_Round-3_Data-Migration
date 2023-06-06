import configparser

class ConfigClass:
    def __init__(self) -> None:
        self.config = configparser.ConfigParser()
        self.config.read('keys.conf')    
        self.config.optionxform

    def load_config(self,profile='DEFAULT'):
        """
        Loading the configuration file
        """                 
        if not self.config.has_section(profile) and profile!='DEFAULT':    
            raise Exception("Profile \'"+ profile +"\' does not exists")        
        return self.config[profile]

    def mod_values(self):
        """
        Return array of values to be config
        """    
        print(self.config['MOD_VALUES'])
        for i in self.config['MOD_VALUES']:
            if i.lower()=='default_header':
                break
            print(i)
        return self.config['MOD_VALUES']

