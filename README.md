# pi_bomb_game

Code to control the RaspberryPi fake bomb box.  This controls a small ADA Fruit 7 Segment display with an I2C backpack and a takes input from multiple buttons and a master control switch.


## bomb_controller.py

The main controlling logic for the "bomb".  It is listening to all the button events and controls the game logic.  On successful "arming" and "defusal" it will send a REST call to the server to start or stop a timer. Techinacally, the "stop" timer is just a 0 second timer.

This module also controls starting the [button_blink_thread](https://github.com/javaplus/pi_bomb_game/blob/master/button_blink_thread.py) module that causes the buttons to blink.

It also causes the buttons to stop and then the button used to "arm" the device to light solid.


