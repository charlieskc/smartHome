
# Turn your Raspberry Pi as Smart Home Control Center and integrate with IFTTT and Alexa 
@Author - Kai Ching Siu, Charlie, 2017

## Introduction
This notebook is to illustrate how to turn the Raspberry Pi to smart home control center. In the following section we will show you how we can use the Pi to control the heater based on the temperature. we will also integrate with IFTTT to enable your rasberry talks to others Apps such as Alexa to provide voice control over your Pi. Cosnider the following scenario:

1. If the room temperate drops to 20 degree, turn on the heater until it goes up to 26 degree
2. Voice command using Alexa Echo Dot - "Alexa, trigger the fan"


## Hardware 
Raspberry Pi 3
Pi Sense Hat (Temperature module) at https://www.raspberrypi.org/products/sense-hat/
Irdroid-Rpi infrared Transceiver at http://www.irdroid.com/irdroid-rpi-infrared-transceiver/
Amazon Echo Dot (If you want to use voice control)

## Raspberry Library Installation
### 1. Install lirc
Do enable the Raspberry PI sending infra-red signal we need to install lirc. 

```bash
sudo apt-get install lirc
```
https://www.hackster.io/austin-stanton/creating-a-raspberry-pi-universal-remote-with-lirc-2fd581

### 2. Install flask
Flask is a python web framework that enables you to implement a RestFul web server in a very simple way

```bash
pip install flask
```

## Setup
### 1. Infra-red lirc setup

#### learn the infra-red signal
sudo service lirc restart
sudo irrecord --device=/dev/lirc0
sudo irrecord -d /dev/lirc0  /etc/lirc/lircd.conf

#### test infrared command

### 2. Web server setup

#### Testing RESTFul Request

### 3. Integrate with IFTTT
We use the IFTTT Maker service to integrate with our PI. Maker service is a simple web request server that allow other service, such as Alexa, to send a webrequest to your Rasberry PI

In order to acheive it you must set your web server internet accessible. Port forward is needed in this case. 






