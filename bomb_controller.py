import paho.mqtt.client as mqtt
import logging
import sys
import button_blink_thread
import setbomb
from subprocess import Popen
import subprocess

running_thread = {}
timer_process_id = None
defuse_button = None

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")
    client.subscribe("events/button")



# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" Message:Payload="+str(msg.payload))
    global running_thread
    global defuse_button
    if msg.payload == "master_switch_ON": 
    	blink()
    if msg.payload == "master_switch_OFF":
        for key in running_thread:
       	    running_thread[key].stop()	
    if msg.payload.startswith("button"):
	print("Button press event detected!")
	global timer_process_id

	if defuse_button is None:
		timer_process_id = Popen(["sudo", "python","/home/pi/workspace/pi_timer_python/mqtt_server.py"]).pid 
		print("timer process=" + str(timer_process_id))
		setbomb.submitTime()	  
		defuse_button = msg.payload
	else:
		print("killing process"+ str(timer_process_id))
		status =subprocess.call(["sudo", "kill","-9",str(timer_process_id)])
		print("status" + str(status))


def blink():
    logging.info("in blink:")
    makeButtonBlink(25)
    makeButtonBlink(18)
    makeButtonBlink(22)
    makeButtonBlink(6)
    
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
