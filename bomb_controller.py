import paho.mqtt.client as mqtt
import logging
import sys
import button_blink_thread
import setbomb
from subprocess import Popen
import subprocess
import os
import signal
import time
import urllib2
import json
import RPi.GPIO as GPIO
try:
    import display_7segment as display
except BaseException as ex:
    print(ex.message)
    pass

running_thread = {}
timer_process_id = None
defuse_button = None
time_delay = 1 
take_input = False
serverIP = os.environ['pi_server_ip']

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("events/button")



# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" Message:Payload="+str(msg.payload))
    global take_input
    global running_thread
    global defuse_button
    global time_delay
    if msg.payload == "master_switch_ON": 
	take_input = True
    	blink()
    if msg.payload == "master_switch_OFF":
	take_input = False
        for key in running_thread:
       	    running_thread[key].stop()	
	#if bomb is defused and we switch it off clear display
	if defuse_button is None:
		display.clear()
		display.writeToDisplay('')
    if msg.payload.startswith("button") and time_delay < time.time() and take_input:
	print("Button press event detected!")
	global timer_process_id
        buttonLEDpin = msg.payload.split(':')[1] 
	if defuse_button is None:
		timer_process_id = Popen(["sudo", "python","/home/pi/workspace/pi_timer_python/mqtt_server.py"],preexec_fn=os.setsid).pid 
		print("timer process=" + str(timer_process_id))
		setbomb.submitTime()	  
		defuse_button = msg.payload
		take_input = False # require the switch to be turned off and on again before taking input
		#stop blinking lights
	        lightUpButton(buttonLEDpin)	
	elif defuse_button == msg.payload:
		print("killing process"+ str(timer_process_id))
		status =os.killpg(os.getpgid(timer_process_id),signal.SIGTERM)
		defuseSuccess(buttonLEDpin)
		defuse_button = None
		take_input = False
		display.writeToDisplay('----')
	else:
		defuseFailure()	
		time_delay = time.time() + 15
    else:
	print("ignoring button during lockout:" + msg.payload)

def defuseFailure(): 
	data = { "say":"Bomb defusal failure! Bomb defusal failure! Lock out for 15 seconds", "parms" : "-s 140 -ven-us+f3"}
        
	req = urllib2.Request('http://' + serverIP +':5000/say')
	req.add_header('Content-Type', 'application/json')

	response = urllib2.urlopen(req, json.dumps(data))

def defuseSuccess(pinLED): 
	lightUpButton(pinLED)
	data = { "say":"Bomb has been defused! Bomb has been defused! Stop, Stop, Stop, Stop stop stop", "parms" : "-s 140 -ven-us+f3"}
        
	req = urllib2.Request('http://'+ serverIP +':5000/say')
	req.add_header('Content-Type', 'application/json')

	response = urllib2.urlopen(req, json.dumps(data))
	time.sleep(1)
	response = urllib2.urlopen(req, json.dumps(data))



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

def lightUpButton(pinId):
	global running_thread
	for key in running_thread:
        	running_thread[key].stop()

	GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
       	GPIO.setup(int(pinId), GPIO.OUT)   # Set LedPin's mode is output
    	GPIO.output(int(pinId), GPIO.HIGH)  # led on



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
