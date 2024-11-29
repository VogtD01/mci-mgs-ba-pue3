import time
from machine import Pin

led_pin = Pin(2, Pin.OUT)
led_pin1 = Pin(13, Pin.OUT)
led_pin2 = Pin(12, Pin.OUT)
led_pin3 = Pin(14, Pin.OUT)
knightrider=3     #hinweis

while 1:
  print('Congratulation Dominic, the setup works')
  led_pin.value(1)    # setzt den pin auf high
  for i in [1,2,3,4,5,6,7]:
    print(i&1)
    print(i&2)
    print(i&4)
    led_pin1.value((i&1)==1) 
    led_pin2.value((i&2)==2)
    led_pin3.value((i&4)==4)    
    time.sleep(1)