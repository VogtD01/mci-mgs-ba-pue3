import time
from machine import Pin

# Set GPIO2 to output
led_pin = Pin(2, Pin.OUT)

while 1:
  print('Congratulation, the setup works')
  
  led_pin.value(1)
  time.sleep(1)

  led_pin.value(0)
  time.sleep(1)