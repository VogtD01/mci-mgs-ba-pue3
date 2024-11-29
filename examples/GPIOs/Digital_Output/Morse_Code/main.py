from machine import Pin
import libs.morsecode as morsecode
import time


# Set GPIO2 to output
led_pin = Pin(2, Pin.OUT)

while 1:
  print("Test and check1")
  morsecode.send("SOS")


  
  