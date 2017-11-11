from threading import Thread
import time
import RPi.GPIO as GPIO

LedPin = 25    # pin

class BlueThread(Thread):
    def __init__(self):
        self.running = False

	super(BlueThread, self).__init__()

    def start(self):
        self.running = True
        super(BlueThread, self).start()

    def run(self):
	
	global LedPin
	  	
	while True:
		GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
        	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output

    		GPIO.output(LedPin, GPIO.HIGH)  # led on
    		time.sleep(1)
    		GPIO.output(LedPin, GPIO.LOW) # led off
    		time.sleep(1)


    def stop(self):
	self.clean()
        self.running = False


    def clean(self):
	
        global LedPin
	GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
  	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output 
        GPIO.output(LedPin, GPIO.LOW)   # led off
        GPIO.cleanup()
