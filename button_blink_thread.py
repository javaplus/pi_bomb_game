from threading import Thread
import time
import RPi.GPIO as GPIO


class BlinkThread(Thread):
    def __init__(self,LEDPIN):
        self.running = False
	self.LedPin = LEDPIN
	super(BlinkThread, self).__init__()

    def start(self):
        self.running = True
        super(BlinkThread, self).start()

    def run(self):
	  	
	while self.running:
		GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
        	GPIO.setup(self.LedPin, GPIO.OUT)   # Set LedPin's mode is output

    		GPIO.output(self.LedPin, GPIO.HIGH)  # led on
    		time.sleep(1)
    		GPIO.output(self.LedPin, GPIO.LOW) # led off
    		time.sleep(1)


    def stop(self):
        self.running = False
	time.sleep(1) #give a second for loop to stop
	self.destroy()


    def destroy(self):
	
	GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
  	GPIO.setup(self.LedPin, GPIO.OUT)   # Set LedPin's mode is output 
        GPIO.output(self.LedPin, GPIO.LOW)   # led off
        GPIO.cleanup()
