import paho.mqtt.client as mqtt
import logging
import os


serverIP = os.environ['pi_server_ip']

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")
    client.subscribe("events/global")


def broadcastEvent(eventName):
    mqttc = mqtt.Client("buttonMachine")
    #mqttc.connect("10.0.0.1", 1883)
    mqttc.connect("localhost", 1883)
    # don't retain messages, this needs to be more real -time
    mqttc.publish("events/button", payload=str(eventName),qos=0,retain=False) 
    mqttc.loop(2) #timeout = 2s
    
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    broadcastEvent(msg.payload)
    


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(serverIP, 1883, 60)
#client.connect("192.168.1.112", 1883, 60)


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
