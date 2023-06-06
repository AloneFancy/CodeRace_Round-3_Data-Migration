from bs4 import BeautifulSoup
import re
import globals
def resolve_html_code(html):
    """
    Resolve Html code
    """    
    return BeautifulSoup(html,features="html.parser").get_text()

def RSTfile(data):
    """
    Extract data in json to formatted RST file
    """
    Raw_file="\n"
    Raw_file+="="*len(data["Module Name"]) + "\n"
    Raw_file+=data["Module Name"] + "\n"
    Raw_file+="="*len(data["Module Name"]) 
    
    for scope in data["List Artifact Info"]:
            if scope["Attribute Type"]=="Heading":
                Raw_file+="\n"*2 +scope["Title"] + '\n' + len(scope["Title"])*'*'
            elif scope["Attribute Type"]=="Information":
                Raw_file+='\n'*2 + '.. sw_req::\n'
                Raw_file+='   :id: '+str(scope["Identifier"]) +'\n'
                Raw_file+='   :artifact_type: Information' + 2*'\n'
                
                substring = scope["ReqIF.Text"].replace("<br","\n|")
                substring = substring.replace("/>","")
                regex = re.compile("xmlns=\".*\"")
                substring = re.sub(regex,'', substring)
                Raw_file+=resolve_html_code(substring)
            else:
                Raw_file+='\n'*2 + '.. sw_req::\n'
                Raw_file+='\t:status: '+str(scope["Status"]) +'\n'
                Raw_file+='\t:id: '+str(scope["Identifier"]) +'\n'            
                Raw_file+='\t:safety_level: '+str(scope["Safety Classification"]) +'\n'
                Raw_file+='\t:artifact_type: '+str(scope["Attribute Type"]) +'\n'
                Raw_file+='\t:crq: '+str(scope["CRQ"]) +'\n'
                Raw_file+= 2*'\n'+'\t'+scope["Title"] + '\n'
                if scope['Attribute Type']=='MO_FUNC_REQ':
                    regex = re.compile("xmlns=\".*\"")
                    substring = scope['ReqIF.Text'].replace("\u00a0","\n")
                    Raw_file+='\n'+ resolve_html_code(substring)
                    
                Raw_file+='\n'*2 + '   .. verify::\n\n'
                Raw_file+=         "\t\t"+re.sub('\n','\n\t\t',scope["Verification Criteria"])

    return Raw_file

def return_key(long_name):
    """
    Convert string values to keys (long_name is how you access attribute of keys)
    """    
    loaded_config = globals.loaded_config
    current_config = globals.current_config
    if loaded_config[current_config].get(long_name):
        if loaded_config[current_config].get(long_name)!='NULL':
            return loaded_config[current_config].get(long_name)
        elif loaded_config[current_config].get(long_name)=='NULL':
            return None
    return long_name

