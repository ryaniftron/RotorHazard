#########################
# Established MQTT Topics
#########################

# These topics contain the topic headers and then what variables are substituted in later.
# If the topic doesn't have any substitute params, 2nd param is None

    ### ClearView Topics v1 ###
        # Publish Topics

# Send command to all receivers
receiver_command_all = "rx/cv1/cmd_all"

# Send command to a node_number
receiver_command_node_topic = ("rx/cv1/cmd_node/%d","node_number")

# Send command to a specific receiver
receiver_command_targeted_topic = ("rx/cv1/cmd_target/%s","receiver_serial_num")

# Send a kick command to a specific receiver (leave the network)
receiver_kick_topic = ("rx/cv1/kick/%s","receiver_serial_num")

# Send an active promotion or demotion to a specific receiver
receiver_active_topic = ("rx/cv1/active/%s","receiver_serial_num")

# Make a request to all receivers (all receivers reply)
receiver_request_all_topic = ("rx/cv1/req_all", None)

# Make a request to all nodes at a node number (all nodes at that node_number reply)
receiver_request_node_all_topic = ("rx/cv1/req_node_all/%d", "node_number")

# Make a request to the active node at a node index
# Only the active receiver at that node replies
receiver_request_node_active_topic = ("rx/cv1/req_node_active/%d", "node_number")

# Make a request to a specific receiver
receiver_request_targeted_topic = ("rx/cv1/req_target/%s","receiver_serial_num")



        # Subscribe Topics

# Response for all
receiver_response_all_topic = ("rx/cv1/resp_all", None)

# Response for a node number
receiver_response_node_topic = ("rx/cv1/resp_node/%s", "+")

# Response for a specific recevier
receiver_response_targeted_topic = ("rx/cv1/resp_target/%s", "+")

# Connection status for receivers
receiver_connection_topic = ("rxcn/%s", "+")

# TODO status topics

mqtt_publish_topics = {
    "cv1" :
        {
            "receiver_command_all":receiver_command_all,
            "receiver_command_node_topic":receiver_command_node_topic,
            "receiver_command_targeted_topic":receiver_command_targeted_topic,
            "receiver_request_node_all_topic":receiver_request_node_all_topic,
            "receiver_request_node_active_topic":receiver_request_node_active_topic,
            "receiver_request_targeted_topic":receiver_request_targeted_topic,
            "receiver_kick_topic":receiver_kick_topic
        }
}

mqtt_subscribe_topics = {
    "cv1" :
        {
            "receiver_response_all":receiver_response_all_topic,
            "receiver_response_node":receiver_response_node_topic,
            "receiver_connection":receiver_connection_topic,
            "receiver_response_targeted":receiver_response_targeted_topic
        }
}