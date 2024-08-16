# NRGKick Integration

A Home Assistant Integration to connect to your NRGKick device.


## Requirements
To be able to setup this integration, you need to have the IP address of the NRGKick.
Within the App (at least version 1.7.7) you need to enable the native web api (JSON).
And finally you need to have firmware version 4.0.0.64 on the NRGKick itself.

## Setup
After installing the intergration in HA, you can configure your NRGkick in HA.
The URL should be 'http://x.x.x.x' where x.x.x.x is replaced by the IP address of your NRGKick device.
It might be good to make sure the IP address is statically configured on your network.

Eventually also configure the Login and Password you chose when configuring the web api via the
NRGKick app.