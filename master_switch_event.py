import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

switch_on = False

def broadcastEvent(eventName):
    mqttc = mqtt.Client("buttonMachine")
    #mqttc.connect("10.0.0.1", 1883)
    mqttc.connect("localhost", 1883)
    # don't retain messages, this needs to be more real -time
    mqttc.publish("events/button", payload=str(eventName),qos=0,retain=False) 
    mqttc.loop(2) #timeout = 2s


while True:
        input_state = GPIO.input(26)
        if input_state == True and switch_on == False:
		switch_on = True
                print('Button Pressed')
                broadcastEvent("master_switch_ON")
                time.sleep(1) # wait a second before we listen for more button presses
	if input_state == False and switch_on == True:
		switch_on = False
		broadcastEvent("master_switch_OFF")

	time.sleep(.2) # waith 200ms before checking switch status
