import time
from machine import Pin, TouchPad

LED=Pin(2,Pin.OUT, drive=Pin.DRIVE_3)
Capacitive_Touch=TouchPad(Pin(33))


while 1:
  print(Capacitive_Touch.read())
  if Capacitive_Touch.read()<400:
    LED.value( not LED.value())
  time.sleep(0.5)
  
  