import paho.mqtt.client as mqtt
import logging
import sys
import button_blink_thread

running_thread = {}

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")
    client.subscribe("events/button")



# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    global running_thread
    if msg.payload == "master_switch_ON": 
    	blink()
    if msg.payload == "master_switch_OFF":
        for key in running_thread:
       	    running_thread[key].stop()	

def blink():
    logging.info("in blink:")
    makeButtonBlink(25)

def makeButtonBlink(ledpin):
    global running_thread

    if ledpin in running_thread:
        running_thread[ledpin].stop()
    running_thread[ledpin] = button_blink_thread.BlinkThread(ledpin)
    running_thread[ledpin].start()



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
#client.connect("10.0.0.1", 1883, 60)
#client.connect("192.168.1.124", 1883, 60)


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
