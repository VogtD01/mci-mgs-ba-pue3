import time
from machine import Pin

# Set GPIO2 to output
led_pin = Pin(2, Pin.OUT)
switch_pin1 = Pin(4,mode=Pin.IN,pull=Pin.PULL_DOWN)
switch_pin2 = Pin(5,mode=Pin.IN,pull=Pin.PULL_UP)

while 1:
  print('Congratulation, the setup works')
  led_pin.value(not switch_pin1.value() ^ switch_pin2.value())
  time.sleep(0.1)