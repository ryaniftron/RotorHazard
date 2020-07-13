#########################
# Established MQTT Topics
#########################

# These topics contain the topic headers and then what variables are substituted in later.
# If the topic doesn't have any substitute params, 2nd param is None

    ### ClearView Topics v1 ###
        # Publish Topics

# Send command to all receivers
receiver_command_all = ("rx/%s/cmd_all", None)

# Send command to a node_number
receiver_command_node_topic = ("rx/%s/cmd_node/%s","node_number")

# Send command to a specific receiver
receiver_command_targeted_topic = ("rx/%s/cmd_target/%s","receiver_serial_num")

# Send a kick command to a specific receiver (leave the network)
receiver_kick_topic = ("rx/%s/kick/%s","receiver_serial_num")

# Send an active promotion or demotion to a specific receiver
receiver_active_topic = ("rx/%s/active/%s","receiver_serial_num")

# Make a request to all receivers (all receivers reply)
receiver_request_all_topic = ("rx/%s/req_all", None)

# Make a request to all nodes at a node number (all nodes at that node_number reply)
receiver_request_node_all_topic = ("rx/%s/req_node_all/%s", "node_number")

# Make a request to the active node at a node index
# Only the active receiver at that node replies
receiver_request_node_active_topic = ("rx/%s/req_node_active/%s", "node_number")

# Make a request to a specific receiver
receiver_request_targeted_topic = ("rx/%s/req_target/%s","receiver_serial_num")

# All command topic for ESP commands
receiver_command_esp_all = ("rx/%s/cmd_esp_all", None)

# Send command to a node_number
receiver_command_esp_node_topic = ("rx/%s/cmd_esp_node/%s","node_number")

# Send command to a specific receiver
receiver_command_esp_targeted_topic = ("rx/%s/cmd_esp_target/%s","receiver_serial_num")



        # Subscribe Topics

# Response for all
receiver_response_all_topic = ("rx/%s/resp_all", None)

# Response for a node number
receiver_response_node_topic = ("rx/%s/resp_node/%s", "+")

# Response for a specific recevier
receiver_response_targeted_topic = ("rx/%s/resp_target/%s", "+")

# Connection status for receivers
receiver_connection_topic = ("rxcn/%s", "+")

# Receiver static status
receiver_status_static_topic = ("status_static/%s", "+")

# Request variable status
receiver_status_variable_topic = ("status_variable/%s", "+")

receiver_protocols = ["cv1", "rf1"]

mqtt_publish_topics = {
    "cv1" :
        {
            "receiver_command_all":receiver_command_all%("cv1"),
            "receiver_command_node_topic":receiver_command_node_topic%("cv1", "%d"),
            "receiver_command_targeted_topic":receiver_command_targeted_topic%("cv1", "%d"),
            "receiver_request_all_topic":receiver_request_all_topic%("cv1"),
            "receiver_request_node_all_topic":receiver_request_node_all_topic%("cv1", "%d"),
            "receiver_request_node_active_topic":receiver_request_node_active_topic%("cv1", "%d"),
            "receiver_request_targeted_topic":receiver_request_targeted_topic%("cv1", "%s"),
            "receiver_kick_topic":receiver_kick_topic%("cv1", "%d"),
            "receiver_command_esp_all": receiver_command_esp_all%("cv1"),
            "receiver_command_esp_node_topic":receiver_command_esp_node_topic%("cv1", "%d"),
            "receiver_command_esp_targeted_topic": receiver_command_esp_targeted_topic%("cv1", "%s"),
        },
    "rf1":
        {
            "receiver_command_all":receiver_command_all%("rf1"),
            "receiver_command_node_topic":receiver_command_node_topic%("rf1", "%d"),
            "receiver_command_targeted_topic":receiver_command_targeted_topic%("rf1", "%d"),
            "receiver_request_all_topic":receiver_request_all_topic%("rf1"),
            "receiver_request_node_all_topic":receiver_request_node_all_topic%("rf1", "%d"),
            "receiver_request_node_active_topic":receiver_request_node_active_topic%("rf1", "%d"),
            "receiver_request_targeted_topic":receiver_request_targeted_topic%("rf1", "%s"),
            "receiver_kick_topic":receiver_kick_topic%("rf1", "%d"),
            "receiver_command_esp_all": receiver_command_esp_all%("rf1"),
            "receiver_command_esp_node_topic":receiver_command_esp_node_topic%("rf1", "%d"),
            "receiver_command_esp_targeted_topic": receiver_command_esp_targeted_topic%("rf1", "%s"),
        }
}

import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(mqtt_publish_topics)

print('abc%sdef%sghi'%(23,'%s'))

mqtt_subscribe_topics = {
    "cv1" :
        {
            "receiver_response_all":receiver_response_all_topic%("cv1"),
            "receiver_response_node":receiver_response_node_topic%("cv1", "%d"),
            "receiver_connection":receiver_connection_topic,
            "receiver_response_targeted":receiver_response_targeted_topic%("cv1", "%s"),
            "receiver_static_status":receiver_status_static_topic,
            "receiver_variable_status":receiver_status_variable_topic
        },
    "rf1" : 
        {
            "receiver_response_all":receiver_response_all_topic%("cv1"),
            "receiver_response_node":receiver_response_node_topic%("cv1", "%d"),
            "receiver_connection":receiver_connection_topic,
            "receiver_response_targeted":receiver_response_targeted_topic%("cv1", "%s"),
            "receiver_static_status":receiver_status_static_topic,
            "receiver_variable_status":receiver_status_variable_topic
        }
}

ESP_COMMANDS = {
    "Request Static Status": "status_static?",
    "Request Variable Status": "status_var?",
    "Set Node Number": "node_number=%d",
}