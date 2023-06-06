#!/usr/bin/env python

import globals
from convert import *
import json, os
import sys


def check_os():
    global PATH
    if os.name == "nt":
        PATH = "output\\"
    elif os.name == "posix":
        PATH = "output/"


def write_to_json_file(data):
    try:
        with open(PATH + "data.json", "w") as f:
            json.dump(data, f, indent=4)
        f.close()
    except:
        raise Exception(
            "No permission to write file or check if output folder is created"
        )


def write_to_rst_file(data):
    rst_file = RSTfile(data)
    try:
        with open(PATH + "ECU_Req.rst", "w") as f:
            f.flush()
            f.write(rst_file)
        f.close()
    except:
        raise Exception(
            "No permission to write file or check if output folder is created"
        )


def create_output_folder():
    """
    Create output folder if not existed
    """
    path = "output"
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)


class ReqIF_Reader:
    """
    Attributes:
        Data_in_json: Return data  in json type after extracting Reqif file
    """

    def __init__(self):
        """
        Ready data to store in json file
        """
        loaded_config = globals.loaded_config
        temp_data = {}
        temp_data[loaded_config.get("Module Name")] = globals.specifications[0].long_name
        temp_data[loaded_config.get("Module Type")] = globals.spec_types[1].long_name
        print(temp_data)
        ListArtifactInfo = self.extract_keys_values()
        temp_data[loaded_config.get("List Artifact Info")] = ListArtifactInfo
        self.Data_in_json = temp_data

    def read_json_file(self, path):
        """
        Read Json data from path
        """
        f = open(path, mode="r")
        data = json.load(f)
        f.close()
        return data

    def extract_keys_values(self):
        """
        Variables guide:
            list{'identifier':{obj:json{}}}
            Output final : [list['identifier']]
        """
        list = {}
        loaded_config = globals.loaded_config
        for iterate in globals.spec_objects:
            obj = {}
            reference = globals.reqif_bundle.get_spec_object_by_ref(iterate.identifier)
            obj[
                loaded_config.get("Attribute Type")
            ] = globals.reqif_bundle.get_spec_object_type_by_ref(
                reference.spec_object_type
            ).long_name
            obj[loaded_config.get("Modified On")] = iterate.last_change
            obj[loaded_config.get("Description")] = (
                iterate.description if iterate.description else ""
            )

            for key in iterate.attribute_map:
                def_ref = iterate.attribute_map.get(key).definition_ref
                keys_values = self.process_value(
                    return_key(globals.def_dictionary[def_ref]),
                    iterate.attribute_map.get(key).value,
                )
                if len(keys_values) > 1:
                    obj[keys_values[0][0]] = keys_values[0][1]
                    obj[keys_values[1][0]] = keys_values[1][1]
                else:
                    obj[keys_values[0][0]] = keys_values[0][1]
            ### pop junk content
            obj.pop(None)
            ### enlist each obj with its own identifier
            list[iterate.identifier] = obj
        final = []
        ### Sort "list[]"" as Hierarchy instruction to "final[]"
        for iterate in globals.specifications:
            for current_hierarchy_node in globals.hierachy(iterate):
                final.append(list[current_hierarchy_node.spec_object])
        return final

    def process_value(self, key, value):
        """
        Resolve value for each key.
        Return [[key,value]]
        To access: [0][0] for key [0][1] for value
        In case ReqIF.Name we can also use value for ReqIF.Text  [0]->ReqIf.Text; [1]->ReqIF.Name
        """
        enum_dictionary = globals.enum_dictionary
        loaded_config = globals.loaded_config
        if key == loaded_config.get("ReqIF.ForeignID"):
            return [[key, int(value)]]
        elif key == loaded_config.get("ReqIF.Name"):
            return [
                [loaded_config.get("ReqIF.Text"), value],
                [key, resolve_html_code(value)[:-2]],
            ]
        elif key == loaded_config.get("Safety Classification"):
            return [[key, enum_dictionary[value[0]]]]
        elif key == loaded_config.get("Status"):
            return [[key, enum_dictionary[value[0]]]]
        return [[key, value]]
    
    def config_values(self,values_to_modify):        
        for object in values_to_modify:
            if object.upper() == 'DEFAULT_HEADER':
                break
                      

            
if __name__ == "__main__":
    if len(sys.argv) == 1:
        globals.load_profile()
    elif len(sys.argv) == 2:
        globals.load_profile(sys.argv[1])
    else:
        raise Exception("Too many arguments")
    check_os()
    create_output_folder()
    globals.init()
    ### TASK 1
    values_to_modify = globals._config.mod_values()
    data_in_json = ReqIF_Reader()
    #data_in_json.config_values(values_to_modify)
    write_to_json_file(data_in_json.Data_in_json)

    ### TASK 2
    write_to_rst_file(data_in_json.Data_in_json)
    """
    Read json file, return rst file
    """
    data = data_in_json.read_json_file(PATH + "data.json")
    rst_file_path = "ECU_Requirement.rst"
    ### TASK 3
