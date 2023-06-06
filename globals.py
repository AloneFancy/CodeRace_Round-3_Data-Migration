from reqif.parser import ReqIFParser
import config

global spec_types, spec_objects, data_types, specifications, hierachy, reqif_bundle
global current_config_profile, loaded_config


def load_config(profile=None):
    global current_config_profile, loaded_config    
    if not profile:
        current_config_profile = "DEFAULT"
    else:
        current_config_profile = profile
    loaded_config = config.load_config(current_config_profile)


def init_spec_dictionary():
    """
    Init types dictionary to lookup by identifiers
    """
    global def_dictionary
    def_dictionary = {}
    for type in spec_types:
        try:
            for key in type.attribute_map:
                def_dictionary[
                    type.attribute_map.get(key).identifier
                ] = type.attribute_map.get(key).long_name
        except:
            pass


def init_enum_dictionary():
    """
    Init enum dictionary for data types to lookup by identifiers
    (Currently only accept T_Status and **T_Safety Classification**)
    """
    global enum_dictionary
    enum_dictionary = {}
    for data_definition in data_types:
        if (
            data_definition.long_name == "T_Status"
            or data_definition.long_name == "T_Safety Classification"
        ):
            for enum in data_definition.values:
                enum_dictionary[enum.identifier] = enum.long_name


def init():
    """
    Initialize global variables
    """
    global spec_types, spec_objects, data_types, specifications, hierachy, reqif_bundle

    input_file_path = "Requirements.reqif"
    reqif_bundle = ReqIFParser.parse(input_file_path)
    ### Global variables' definitions
    spec_objects = reqif_bundle.core_content.req_if_content.spec_objects
    spec_types = reqif_bundle.core_content.req_if_content.spec_types
    data_types = reqif_bundle.core_content.req_if_content.data_types
    specifications = reqif_bundle.core_content.req_if_content.specifications
    hierachy = reqif_bundle.iterate_specification_hierarchy
    init_spec_dictionary()
    init_enum_dictionary()
