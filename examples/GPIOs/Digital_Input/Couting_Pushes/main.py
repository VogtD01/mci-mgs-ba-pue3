import time
from machine import Pin

# Set GPIO2 to output
led_pin = Pin(2, Pin.OUT)
switch_pin1 = Pin(4,mode=Pin.IN,pull=Pin.PULL_DOWN)
counter=0

print('Congratulation, the setup works')
while 1:
  if switch_pin1.value():
    counter=counter+1
    # time.sleep(0.2) #... Sleep Deboucing
    print(counter)
    led_pin.value(switch_pin1.value())
  

  # Sleep Debouncing has the major problem of "wasting" time, the MCU cannot do anything else but sleeping for 0.2 seconds