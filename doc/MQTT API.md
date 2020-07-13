# RH MQTT API

This document serves to detail the MQTT API that is supported by RotorHazard. Both the topics and implementation details of messaging are shared. This can be used as a template to integrate other recievers with RotorHazard timing. 

The topic definitions supported by RH are in `src/server/mqtt_topics.py`. RH will publish to _mqtt_publish_topics_ and subscribe to _mqtt_subscribe_topics_. Thus, for a device to communicate with RH, these topic definitions are flipped.

## Initial Connection

To connect to the RH network, an external device should publish to the topic _receiver_connection_topic/\<serial_number\>, where \<serial_number\> is a unique ID of the external device. Ensure these are unique; a common method is using the MAC address of the WiFi chip of the device. This topic should set to be the lastwill topic, with QOS _1_, and retain _True_. That way, when the external device is turned off, a disconnect message is sent to all devices. It is also recommeneded to decrease the lastwill_time to _10_ seconds.  

* Example Topic: `rxcn/CV_AEB2CD5FB1`
* Example Message: `1` or `0` for connected and disconnected respectively

## Status Messages

Status messages are how RH queries external devices for their status.
 
### Static Status

The static status is used to inform RH of the external devices capabilities. The data in the status_static never changes when the external devices is running, however it may change over a device restart. For example, the external device may be updated OTA, so its firmware version will change. When requested for static status, the external device should respond with a JSON payload encoding a few key parameters:

* Device (mandatory)
    * Indicates device type, for example if it is a video receiver.
    * Key: 'dev'
    * Options ['rx',]
* Version (optional)
    * Indicates the version of software running on the wireless dongle
    * Key: 'ver'
    * Example: '1.0.1_Beta'
* Firmware (mandatory)
    * Indicates what the firmware version of the external device is
    * Key: 'fw'
    * Example: '1.20a' for ClearView's 1.20a firmware

* Friendly Name
    * Indicates a more user friendly "nickname" for a unit
    * Key: 'fn'
    * Example: 'Ryan CV2.0'
    * TODO update RH and CV to use fn instead of nn for this



* RH Requests Static Status on any of the _receiver_command_esp_* topics. 
  * For this example, it is requesting static status of a receiver ('rx') running clearview API v1 (cv1) with serial number 'CV_AEB2CD5FB1'. It knows the serial number from the initial connection message.
  * Topic Example: `rx/cv1/cmd_esp_target/CV_AEB2CD5FB1`
  * Message: `status_static?`, as defined in mqtt_topics.ESP_COMMANDS

* External Device Reply
    * It is recommend to always reply to the topic name of the specific device where the serial number is encoded in the topic name
    * Topic Example: `status_static/CV_AEB2CD5FB1`
    * Message: `{"dev":"rx",  "ver":"1.0.1_Beta",  "fw":"1.20a",  "fn":"Ryan CV2.0"}`


### Variable Status

The variable status is used to inform RH of external device data that can change while running, but is tied to the wireless dongle. For example, a video receiver may change what node number it is on, but the ClearView receiver itself has no knowledge of the node number. As a rule of thumb, any data exclusively stored in the wireless dongle should be shared here as JSON payload.

* Node Number (mandatory for video receivers)
    * Indicates the node number of the video receiver that it will track
    * Key: 'nn'
    * Options['0','1','2','3','4','5','6','7']

* RH Requests Static Variable on any of the _receiver_command_esp_* topics. 
  * For this example, it is requesting variable status of a receiver ('rx') running clearview API v1 (cv1) with serial number 'CV_AEB2CD5FB1'. It knows the serial number from the initial connection message.
  * Topic Example: `rx/cv1/cmd_esp_target/CV_AEB2CD5FB1`
  * Message: `status_var?`, as defined in mqtt_topics.ESP_COMMANDS

* External Device Reply
    * It is recommend to always reply to the topic name of the specific device where the serial number is encoded in the topic name
    * Topic Example: `status_static/CV_AEB2CD5FB1`
    * Message: `{"nn", "3"}`

## External Device Commands

## External Device Request






