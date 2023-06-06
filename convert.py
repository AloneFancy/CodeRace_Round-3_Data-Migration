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
    loaded_config = globals.loaded_config
    Raw_file = "\n"
    Raw_file += "=" * len(data[loaded_config.get("Module Name")]) + "\n"
    Raw_file += data[loaded_config.get("Module Name")] + "\n"
    Raw_file += "=" * len(data[loaded_config.get("Module Name")])
    for scope in data["List Artifact Info"]:
        if scope[loaded_config.get("Attribute Type")] == "Heading":
            Raw_file += (
                "\n" * 2
                + scope[loaded_config.get("ReqIF.Name")]
                + "\n"
                + len(scope[loaded_config.get("ReqIF.Name")]) * "*"
            )
        elif scope[loaded_config.get("Attribute Type")] == "Information":
            Raw_file += "\n" * 2 + ".. sw_req::\n"
            Raw_file += (
                "   :id: " + str(scope[loaded_config.get("ReqIF.ForeignID")]) + "\n"
            )
            Raw_file += "   :artifact_type: Information" + 2 * "\n"

            substring = resolve_html_code(scope[loaded_config.get("ReqIF.Text")])
            substring = substring.replace("\n", "\n\t")
            substring = substring.replace("\\", "|")
            Raw_file += "\t" + substring[:-2]
        else:
            Raw_file += "\n" * 2 + ".. sw_req::\n"
            Raw_file += "\t:status: " + str(scope[loaded_config.get("Status")]) + "\n"
            Raw_file += (
                "\t:id: " + str(scope[loaded_config.get("ReqIF.ForeignID")]) + "\n"
            )
            Raw_file += (
                "\t:safety_level: "
                + str(scope[loaded_config.get("Safety Classification")])
                + "\n"
            )
            Raw_file += (
                "\t:artifact_type: "
                + str(scope[loaded_config.get("Attribute Type")])
                + "\n"
            )
            Raw_file += "\t:crq: " + str(scope[loaded_config.get("CRQ")]) + "\n"

            if (
                scope[loaded_config.get("Attribute Type")] == "MO_FUNC_REQ"
                or scope[loaded_config.get("Attribute Type")] == "MO_NON_FUNC_REQ"
            ):
                substring = scope[loaded_config.get("ReqIF.Text")]
                substring = "\n" + resolve_html_code(substring)
                regex = re.compile("\n")
                substring = substring.replace("\n", "\n\t")
                substring = substring.replace("\\", "|")
                Raw_file += "\n\t" + substring[:-2]
            else:
                Raw_file += (
                    2 * "\n" + "\t" + scope[loaded_config.get("ReqIF.Name")] + "\n"
                )

            Raw_file += "\n" * 2 + "   .. verify::\n\n"
            Raw_file += "\t\t" + re.sub(
                "\n", "\n\t\t", scope[loaded_config.get("Verification Criteria")]
            )

    return Raw_file


def return_key(long_name):
    """
    Convert string values to keys (long_name is how you access attribute of keys)
    """
    loaded_config = globals.loaded_config
    if loaded_config.get(long_name):
        if loaded_config.get(long_name) != "NULL":
            return loaded_config.get(long_name)
        elif loaded_config.get(long_name) == "NULL":
            return None
    return long_name
