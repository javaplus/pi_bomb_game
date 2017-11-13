import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(int(sys.argv[1]), GPIO.IN, pull_up_down=GPIO.PUD_UP)

switch_on = False

def broadcastEvent(eventName):
    mqttc = mqtt.Client("buttonMachine")
    #mqttc.connect("10.0.0.1", 1883)
    mqttc.connect("localhost", 1883)
    # don't retain messages, this needs to be more real -time
    mqttc.publish("events/button", payload=str(eventName),qos=0,retain=False) 
    mqttc.loop(2) #timeout = 2s


while True:
        input_state = GPIO.input(int(sys.argv[1]))
        if input_state == False:
                print('Button Pressed' + str(sys.argv[2]))
                broadcastEvent("button_"+str(sys.argv[2])+":"+str(sys.argv[3]))
                time.sleep(1) # wait a second before we listen for more button presses

	time.sleep(.2) # waith 200ms before checking switch status
