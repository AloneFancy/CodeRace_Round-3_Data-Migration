from reqif.parser import ReqIFParser
from convert import *
import json








if __name__ == "__main__":
    input_file_path = "Requirements.reqif"
    reqif_bundle = ReqIFParser.parse(input_file_path)