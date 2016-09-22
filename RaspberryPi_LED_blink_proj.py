'''
Build a circuit using your Raspberry Pi that causes an LED to blink when a push button is NOT pressed.
However, the LED should stay on continually when the push button IS pressed.
Video should show the LED blinking when the push button is not pressed,
and it should show that the LED is constantly on while the button is pressed.

The code can be tested without Raspberry Pi board by using print statements

'''
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)  #setup or initialize the gpio board
GPIO.setup(27,GPIO.OUT)  #setup led pin 27
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #setup button UP for this project, button up
LED_OFF = False
while True:
    if GPIO.input(4) == True: #if button up, it blinks
      print ("Button NOT Pressed")
      GPIO.output(27, True)
      time.sleep(0.5) #sleep half second
      GPIO.output(27, False)
      time.sleep(0.5)
    else: #if button down, it stays constantly
      print "Button Pressed"
      GPIO.output(27, True)
