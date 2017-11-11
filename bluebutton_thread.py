from threading import Thread
import time
import RPi.GPIO as GPIO


class BlueThread(Thread):
    def __init__(self):
        self.running = False
        super(BlueThread, self).__init__()

    def start(self):
        self.running = True
        super(BlueThread, self).start()

    def run(self):
	LedPin = 25    # pin

  	GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
  	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
  	GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to turn on led


  	while True:
    		GPIO.output(LedPin, GPIO.HIGH)  # led on
    		time.sleep(1)
    		GPIO.output(LedPin, GPIO.LOW) # led off
    		time.sleep(1)


    def destroy():
     	GPIO.output(LedPin, GPIO.LOW)   # led off
  	GPIO.cleanup()                  # Release resource

        

    def stop(self):
	destroy()
        self.running = False
