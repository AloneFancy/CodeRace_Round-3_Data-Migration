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
        temp_data = {}
        temp_data["Module Name"] = globals.specifications[0].long_name
        temp_data["Module Type"] = globals.spec_types[1].long_name
        ListArtifactInfo = self.extract_keys_values()
        temp_data["List Artifact Info"] = ListArtifactInfo
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

        for iterate in globals.spec_objects:
            obj = {}
            reference = globals.reqif_bundle.get_spec_object_by_ref(iterate.identifier)
            obj["Attribute Type"] = globals.reqif_bundle.get_spec_object_type_by_ref(
                reference.spec_object_type
            ).long_name
            obj["Modified On"] = iterate.last_change
            obj["Description"] = iterate.description if iterate.description else ""
            obj["ReqIF.Text"] = ""
            for key in iterate.attribute_map:
                def_ref = iterate.attribute_map.get(key).definition_ref
                obj[return_key(globals.def_dictionary[def_ref])] = self.process_value(
                    return_key(globals.def_dictionary[def_ref]),
                    iterate.attribute_map.get(key).value,
                )
            obj.pop(None)
            list[iterate.identifier] = obj
        final = []
        for iterate in globals.specifications:
            for current_hierarchy_node in globals.hierachy(iterate):
                final.append(list[current_hierarchy_node.spec_object])
        return final

    def process_value(self, key, value):
        """
        Resolve value for each key
        """
        enum_dictionary = globals.enum_dictionary
        loaded_config = globals.loaded_config
        profile = globals.current_config_profile
        if key == loaded_config[profile].get("ReqIF.ForeignID"):
            return int(value)
        elif key == loaded_config[profile].get("ReqIF.Name"):
            return resolve_html_code(value)[:-2]
        elif key == loaded_config[profile].get("Safety Classification"):
            return enum_dictionary[value[0]]
        elif key == loaded_config[profile].get("Status"):
            return enum_dictionary[value[0]]

        return value


if __name__ == "__main__":
    if len(sys.argv) == 1:
        globals.load_config()
    elif len(sys.argv) == 2:
        globals.load_config(sys.argv[1])
    else:
        raise Exception("Too many arguments")
    check_os()
    create_output_folder()
    globals.init()
    ### TASK 1
    data_in_json = ReqIF_Reader()
    write_to_json_file(data_in_json.Data_in_json)
    write_to_rst_file(data_in_json.Data_in_json)
    ### TASK 2
    """
    Read json file, return rst file
    """
    data = data_in_json.read_json_file(PATH + "data.json")
    rst_file_path = "ECU_Requirement.rst"
    ### TASK 3
