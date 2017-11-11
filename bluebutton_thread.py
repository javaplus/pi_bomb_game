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
	  	
	while self.running:
		GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
        	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output

    		GPIO.output(LedPin, GPIO.HIGH)  # led on
    		time.sleep(1)
    		GPIO.output(LedPin, GPIO.LOW) # led off
    		time.sleep(1)


    def stop(self):
        self.running = False
	time.sleep(1) #give a second for loop to stop
	self.destroy()


    def destroy(self):
	
        global LedPin
	GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
  	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output 
        GPIO.output(LedPin, GPIO.LOW)   # led off
        GPIO.cleanup()
