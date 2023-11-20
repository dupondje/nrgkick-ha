# NRGKick Integration

A Home Assistant Integration to connect to your NRGKick device.


## Setup
To be able to use this integration, you currently need to find out your current UUID.
This is the UUID which the NRGKick Android app uses to authenticate with your NRGKick device.

The easiest way is to start a tcpdump capture of the traffic from your phone to the NRGKick.
Open that capture in wireshark with the protobuf_websocket.lua plugin (https://github.com/dupondje/nrgkick-proto) enabled.
And then you can easily find the UUID that is used.

All you still need to do then is adding this integration to HA via HACS and enter the IP and UUID.
And you are ready to go :)
