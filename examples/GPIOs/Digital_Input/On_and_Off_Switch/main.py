import time
from machine import Pin

# Set GPIO2 to output
led_pin = Pin(2, Pin.OUT)
switch_pin = Pin(4,Pin.IN)

while 1:
  print('Congratulation, the setup works')
  
  led_pin.value(0 == switch_pin.value())
  time.sleep(0.1)