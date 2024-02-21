# NRGKick Integration

A Home Assistant Integration to connect to your NRGKick device.


## Setup
To be able to setup this integration, you need to have the IP address of the NRGKick and a UUID or the Serial Number.

### Serial Number
Note down the last 7 numbers of the NRGKick's serial number before the 'SxDx'.
With this number, you can configure the HA Integration.

NOTE: If you configured a PIN code when you first configured the NRGKick app on your phone, you will need to use that PIN code instead of the 7 digits serial number.

The setup phase will create a new unique UUID to be used for the NRGKick Integration in HA.

### UUID
This is the UUID which the NRGKick Android app uses to authenticate with your NRGKick device.

The easiest way is to start a tcpdump capture of the traffic from your phone to the NRGKick.
Open that capture in wireshark with the protobuf_websocket.lua plugin (https://github.com/dupondje/nrgkick-proto) enabled.
And then you can easily find the UUID that is used.
