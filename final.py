from reqif.parser import ReqIFParser
from convert import *
import git_upload
import json
import config

def spec_dictionary():
    '''
    Init def 
    '''
    global def_dictionary
    def_dictionary = {}
    for type in spec_types:
        try:
            for key in type.attribute_map:                
                def_dictionary[type.attribute_map.get(key).identifier]= type.attribute_map.get(key).long_name
        except:
            pass

def enum_dictionary():
    '''
    Init enum dictionary for data types
    '''
    global enum_dictionary
    enum_dictionary={}
    for data_def in data_types:
        if(data_def.long_name=='T_Status'or data_def.long_name=='T_Safety Classification'):            
            for enum in data_def.values:
                enum_dictionary[enum.identifier] = enum.long_name

def extract_to_json(data):
    try:
        with open('data.json', 'w') as f:
            json.dump(data, f)
        f.close()
    except:
        Exception("Wrong path")
def extract_to_rst(data):
    try:
        with open('ECU_Req.rst','w')as f:
            f.flush()
            f.write(RSTfile(data))
        f.close()
    except: 
        Exception("Wrong path")

def read_json_file(path):
    """
    Read Json data from path
    """
    f = open(path)    
    return json.load(f)

def init(reqif_bundle):
    """
    Initialize global variables
    """
    global spec_types, spec_objects,data_types
    input_file_path = "Requirements.reqif"
    reqif_bundle = ReqIFParser.parse(input_file_path)
    ### Global variables
    spec_objects = reqif_bundle.core_content.req_if_content.spec_objects
    spec_types = reqif_bundle.core_content.req_if_content.spec_types
    data_types = reqif_bundle.core_content.req_if_content.data_types

if __name__ == "__main__":   
    init()
    data = {}
    extract_to_json(data)
    
    extract_to_rst(data)
    ### TASK 1
    config.configuration()
    ### TASK 2
    """
    Read json file, return rst file
    """
    data = read_json_file('data.json')
    rst_file_path = 'ECU_Requirement.py'
    ### TASK 3



