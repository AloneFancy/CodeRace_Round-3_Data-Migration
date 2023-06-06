#!/usr/bin/env python

import globals
# from globals import * 
from convert import *
#import git_upload
import json
import config

PATH = './'

def extract_to_json(data):
    try:
        with open(PATH+"output/data.json", "w") as f:
            json.dump(data, f,indent=4)
        f.close()
    except:
        raise Exception("No permission to write file or check if output folder is created")

def extract_to_rst(data):
    rst_file = RSTfile(data)
    try:
        with open(PATH + "output/ECU_Req.rst", "w") as f:
            f.flush()
            f.write(rst_file)
        f.close()
    except:
        raise Exception("No permission to write file or check if output folder is created")

def read_json_file(path):
    """
    Read Json data from path
    """
    f = open(path,mode='r')
    data = json.load(f)
    f.close()
    return data

def extract_keys_values():
    """
    Variables guide:
        list{'identifier':{obj:json{}}}
        Output final : [list['identifier']]
    """
    list={}
     
    for iterate in globals.spec_objects:
        obj={}
        reference = globals.reqif_bundle.get_spec_object_by_ref(iterate.identifier)
        obj["Attribute Type"]=globals.reqif_bundle.get_spec_object_type_by_ref(reference.spec_object_type).long_name
        obj["Modified On"]=iterate.last_change
        obj["Description"]=iterate.description if iterate.description else ""
        obj["ReqIF.Text"]=""
        for key in iterate.attribute_map:
            def_ref = iterate.attribute_map.get(key).definition_ref
            obj[return_key(globals.def_dictionary[def_ref])]=process_value(return_key(globals.def_dictionary[def_ref]),iterate.attribute_map.get(key).value)
        obj.pop(None)
        list[iterate.identifier]=obj
    final = []
    for iterate in globals.specifications:
        for current_hierarchy_node in globals.hierachy(iterate):            
            final.append(list[current_hierarchy_node.spec_object])
    return final

def process_value(key,value):
    """
    Resolve value for each key
    """
    enum_dictionary = globals.enum_dictionary
    if key=='Identifier':
        return int(value)
    elif key=='Title':
        return resolve_html_code(value)
    elif key=='Safety Classification':
        return enum_dictionary[value[0]]                      
    elif key=='Status':
        return enum_dictionary[value[0]]
    elif key==None:
        pass
    return value

def process_data():
    """
    Ready data to store in json file
    """
    temp_data = {}
    temp_data["Module Name"] = globals.specifications[0].long_name
    temp_data["Module Type"] = globals.spec_types[1].long_name
    ListArtifactInfo = extract_keys_values() 
    temp_data["List Artifact Info"] = ListArtifactInfo
    return temp_data

if __name__ == "__main__":
    globals.init()
    data_in_json = process_data()
    extract_to_json(data_in_json)
    extract_to_rst(data_in_json)
    ### TASK 1
    config.configuration()
    ### TASK 2
    """
    Read json file, return rst file
    """
    data = read_json_file("data.json")
    rst_file_path = "ECU_Requirement.py"
    ### TASK 3
