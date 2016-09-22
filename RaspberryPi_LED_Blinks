'''
Build a circuit using your Raspberry Pi that causes an LED to blink when a push button is NOT pressed.
However, the LED should stay on continually when the push button IS pressed.
Video should show the LED blinking when the push button is not pressed,
and it should show that the LED is constantly on while the button is pressed.

The code can be tested without Raspberry Pi board by using print statements

'''
import Rpi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)  #setup or initialize the gpio board
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #setup pin 10 for this project, button up
while True:
  input_state  = GPIO.output(10)
  if input_state == True: #if button up, it blinks
    print ("Button Pressed")
    GPIO.output(10, True)
    time.sleep(0.5) #sleep half second
    GPIO.output(10, False)
    time.sleep(0.5)
else: #if button down, it stays constantly
    print "Button Not Pressed"
    GPIO.output(10, True)
