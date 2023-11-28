import autogen

# Load configurations from OAI_CONFIG_LIST.JS 
config_list = autogen.oai.config_list_from_json(
    "OAI_CONFIG_LIST.JS",
    file_location="."
)

class GroupChat(autogen.GroupChat):
