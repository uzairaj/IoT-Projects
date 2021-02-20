This video is the continuation of previous video in which we send sensor data from Esp8266 to Raspberry Pi. 
In this video we will be sending sensor data from Raspberry Pi to a IoT Cloud (in this case we will use ThingSpeak cloud).
We will also display data in different widgets and graph form on IoT cloud.

Helpful Commands:
-> udo apt-get update
-> sudo apt-get upgrade
-> sudo apt install -y mosquitto mosquitto-clients

-> mosquitto -v
-> mosquitto -d
-> mosquitto_sub -d -t testing
-> mosquitto_pub -d -t testing -m "Good Day!"

-> pip install paho-mqtt

You can check out details tutorial on youtube
https://youtu.be/UvfkzNiVk_A
