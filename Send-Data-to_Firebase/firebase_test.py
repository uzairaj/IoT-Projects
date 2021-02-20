import paho.mqtt.client as mqtt
from firebase import firebase

firebase = firebase.FirebaseApplication('add_your_firebase_application_url', None)

val=''
val2=''
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("/esp8266/temperature")
    client.subscribe("/esp8266/humidity")

def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '" + message.topic)
    
    humi = 0
    temp = 0
    if message.topic == "/esp8266/temperature":
        print("temperature update")
        temp = str(message.payload, 'UTF-8')
        temp = temp.strip()
        print(temp)
        global val
        val = temp
        
    if message.topic == "/esp8266/humidity":
        print("humidity update")
        humi = str(message.payload, 'UTF-8')
        humi = humi.strip()
        print(humi)
        global val2
        val2 = humi
    
    if val != '' and val2 != '':    
        print(val, val2)
        data = {"Temperature": val, "Humidity": val2}
        firebase.post('/sensor/dht', data)
        val = ''
        val2 = ''

def main():
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    
    mqtt_client.connect('localhost', 1883, 60) 
    mqtt_client.loop_start() 

if __name__ == '__main__':
    print('MQTT to InfluxDB bridge')
    main()


