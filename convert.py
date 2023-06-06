import html2text
import re
import globals
def resolve_html_code(html):
    """
    Resolve Html code
    """    
    junk = html2text.HTML2Text()    
    return junk.handle(html)

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
                
                substring = resolve_html_code(scope["ReqIF.Text"])
                substring = substring.replace('\n','\n\t')
                substring = substring.replace('\\','|')
                Raw_file+='\t' + substring[:-2]
            else:
                Raw_file+='\n'*2 + '.. sw_req::\n'
                Raw_file+='\t:status: '+str(scope["Status"]) +'\n'
                Raw_file+='\t:id: '+str(scope["Identifier"]) +'\n'            
                Raw_file+='\t:safety_level: '+str(scope["Safety Classification"]) +'\n'
                Raw_file+='\t:artifact_type: '+str(scope["Attribute Type"]) +'\n'
                Raw_file+='\t:crq: '+str(scope["CRQ"]) +'\n'
                
                if scope['Attribute Type']=='MO_FUNC_REQ' or scope['Attribute Type']=='MO_NON_FUNC_REQ' :               
                    substring = scope['ReqIF.Text']     
                    substring ='\n'+ resolve_html_code(substring)
                    regex = re.compile('\n')
                    substring = substring.replace('\n','\n\t')
                    substring = substring.replace('\\','|')
                    Raw_file+='\n\t'+  substring[:-2]
                else:
                    Raw_file+= 2*'\n'+'\t'+scope["Title"] + '\n'
                    
                Raw_file+='\n'*2 + '   .. verify::\n\n'
                Raw_file+=         "\t\t"+re.sub('\n','\n\t\t',scope["Verification Criteria"])

    return Raw_file

def return_key(long_name):
    """
    Convert string values to keys (long_name is how you access attribute of keys)
    """    
    loaded_config = globals.loaded_config
    profile = globals.current_config_profile
    if loaded_config[profile].get(long_name):
        if loaded_config[profile].get(long_name)!='NULL':
            return loaded_config[profile].get(long_name)
        elif loaded_config[profile].get(long_name)=='NULL':
            return None
    return long_name

